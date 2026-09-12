#!/usr/bin/env python3
"""
Minimal Objective-C 2.0 metadata dumper for 32-bit (armv7) Mach-O binaries.

Written for the Catch Notes 5.2.8 teardown. class-dump and ktool both fail on
this binary: class-dump needs a working Objective-C runtime of the same
architecture, and ktool 2.0.0 mis-parses the armv7 protocol table. This parser
reads the metadata sections directly, so it needs no runtime and no network.

Usage:
    python3 objc_dump32.py <path-to-macho> [--headers <outdir>]
"""

import struct
import sys
import os

U32 = struct.Struct("<I")


class MachO:
    def __init__(self, data):
        self.data = data
        magic = U32.unpack_from(data, 0)[0]
        if magic != 0xFEEDFACE:
            raise ValueError("not a 32-bit little-endian Mach-O (magic %#x)" % magic)
        ncmds = U32.unpack_from(data, 16)[0]
        self.sections = []
        off = 28
        for _ in range(ncmds):
            cmd, cmdsize = struct.unpack_from("<II", data, off)
            if cmd == 0x1:  # LC_SEGMENT
                nsects = U32.unpack_from(data, off + 48)[0]
                soff = off + 56
                for _ in range(nsects):
                    sectname = data[soff:soff + 16].rstrip(b"\0").decode()
                    segname = data[soff + 16:soff + 32].rstrip(b"\0").decode()
                    addr, size, offset = struct.unpack_from("<III", data, soff + 32)
                    self.sections.append((segname, sectname, addr, size, offset))
                    soff += 68
            off += cmdsize

    def va_to_off(self, va):
        for _seg, _sect, addr, size, offset in self.sections:
            if addr <= va < addr + size:
                return offset + (va - addr)
        return None

    def section(self, seg, sect):
        for s in self.sections:
            if s[0] == seg and s[1] == sect:
                return s
        return None

    def u32(self, va):
        off = self.va_to_off(va)
        if off is None:
            return None
        return U32.unpack_from(self.data, off)[0]

    def cstr(self, va):
        off = self.va_to_off(va)
        if off is None:
            return None
        end = self.data.index(b"\0", off)
        return self.data[off:end].decode("utf-8", "replace")


def method_list(m, va):
    """Return [(selector, type_encoding)] from a method_list_t."""
    if not va:
        return []
    entsize = m.u32(va)
    count = m.u32(va + 4)
    if not count or count > 20000:
        return []
    entsize = (entsize or 12) & ~3
    out = []
    for i in range(count):
        e = va + 8 + i * entsize
        name = m.cstr(m.u32(e) or 0)
        types = m.cstr(m.u32(e + 4) or 0)
        if name:
            out.append((name, types or ""))
    return out


def ivar_list(m, va):
    """Return [(name, type_encoding, offset)] from an ivar_list_t."""
    if not va:
        return []
    entsize = m.u32(va)
    count = m.u32(va + 4)
    if not count or count > 20000:
        return []
    entsize = (entsize or 20) & ~3
    out = []
    for i in range(count):
        e = va + 8 + i * entsize
        off_ptr = m.u32(e)
        name = m.cstr(m.u32(e + 4) or 0)
        types = m.cstr(m.u32(e + 8) or 0)
        offset = m.u32(off_ptr) if off_ptr else None
        if name:
            out.append((name, types or "", offset))
    return out


def read_class(m, va, seen=None):
    """Read objc_class_t at va. Returns a dict, or None when unreadable."""
    seen = seen or set()
    if not va or va in seen:
        return None
    seen.add(va)
    isa = m.u32(va)
    superclass = m.u32(va + 4)
    data_ptr = m.u32(va + 16)
    if data_ptr is None:
        return None
    ro = data_ptr & ~3
    name = m.cstr(m.u32(ro + 16) or 0)
    if not name:
        return None
    rec = {
        "name": name,
        "super_va": superclass,
        "instance_methods": method_list(m, m.u32(ro + 20) or 0),
        "ivars": ivar_list(m, m.u32(ro + 28) or 0),
        "class_methods": [],
    }
    meta = read_class(m, isa, seen) if isa else None
    if meta:
        rec["class_methods"] = meta["instance_methods"]
    return rec


def encode_signature(sel, types):
    """Render an Objective-C declaration from a selector and type encoding."""
    ret = types[0] if types else "v"
    simple = {
        "v": "void", "@": "id", ":": "SEL", "#": "Class", "c": "char",
        "i": "int", "s": "short", "l": "long", "q": "long long",
        "C": "unsigned char", "I": "unsigned int", "S": "unsigned short",
        "L": "unsigned long", "Q": "unsigned long long", "f": "float",
        "d": "double", "B": "BOOL", "*": "char *", "^": "void *",
    }
    rtype = simple.get(ret, "id")
    if ":" not in sel:
        return "%s %s;" % (rtype, sel)
    parts = [p for p in sel.split(":") if p != ""]
    return "%s %s;" % (rtype, ":(id)arg:".join(parts) + ":(id)arg")


def main():
    path = sys.argv[1]
    outdir = None
    if "--headers" in sys.argv:
        outdir = sys.argv[sys.argv.index("--headers") + 1]
        os.makedirs(outdir, exist_ok=True)

    with open(path, "rb") as fh:
        m = MachO(fh.read())

    sect = m.section("__DATA", "__objc_classlist")
    if not sect:
        print("no __objc_classlist section", file=sys.stderr)
        return 1
    _seg, _name, addr, size, offset = sect
    classes = []
    for i in range(size // 4):
        va = U32.unpack_from(m.data, offset + i * 4)[0]
        rec = read_class(m, va)
        if rec:
            rec["va"] = va
            classes.append(rec)

    by_va = {c["va"]: c["name"] for c in classes}
    classes.sort(key=lambda c: c["name"])

    for c in classes:
        sup = by_va.get(c["super_va"], "NSObject")
        lines = ["@interface %s : %s" % (c["name"], sup), "{"]
        for name, types, off in c["ivars"]:
            lines.append("    // +%s  %s  %s" % (off, types, name))
        lines.append("}")
        for sel, types in c["class_methods"]:
            lines.append("+ " + encode_signature(sel, types))
        for sel, types in c["instance_methods"]:
            lines.append("- " + encode_signature(sel, types))
        lines.append("@end")
        text = "\n".join(lines)
        if outdir:
            with open(os.path.join(outdir, c["name"] + ".h"), "w") as fh:
                fh.write(text + "\n")
        else:
            print(text + "\n")

    ivars = sum(len(c["ivars"]) for c in classes)
    methods = sum(len(c["instance_methods"]) + len(c["class_methods"]) for c in classes)
    print("// %d classes, %d methods, %d ivars" % (len(classes), methods, ivars),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
