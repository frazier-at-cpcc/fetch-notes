#!/usr/bin/env python3
"""Decode the NIBArchive container format.

This module reads structure and nothing else. It does not know that UIView
exists. Keeping the format layer free of UIKit meaning means a mistaken
interpretation in tools/nib_layout.py never requires editing verified parsing
code.

Format, verified against all 17 NIB files in Catch Notes 5.2.8:

    offset 0   10 bytes   the ASCII magic "NIBArchive"
    offset 10  10 uint32  major, minor, and a (count, offset) pair for each of
                          the object, key, value, and class-name tables

Integers inside the tables use a variable-length encoding of seven bits per
byte in little-endian order, where the byte carrying bit 0x80 terminates.
"""

import dataclasses
import struct
import sys

MAGIC = b"NIBArchive"
_HEADER = struct.Struct("<10I")


class NIBFormatError(Exception):
    """Raised when the input is not a well-formed NIBArchive."""


@dataclasses.dataclass
class Header:
    major: int
    minor: int
    object_count: int
    object_offset: int
    key_count: int
    key_offset: int
    value_count: int
    value_offset: int
    class_count: int
    class_offset: int


def read_varint(data, pos):
    """Return (value, next_pos). The byte with bit 0x80 set ends the integer."""
    value = 0
    shift = 0
    while True:
        try:
            byte = data[pos]
        except IndexError:
            raise NIBFormatError("varint ran past the end of the buffer")
        pos += 1
        value |= (byte & 0x7F) << shift
        shift += 7
        if byte & 0x80:
            return value, pos


def read_header(data):
    """Parse the 50-byte header, raising NIBFormatError on a bad magic."""
    if len(data) < 50 or data[:10] != MAGIC:
        raise NIBFormatError("missing NIBArchive magic")
    return Header(*_HEADER.unpack_from(data, 10))
# Value type tags. Fixed-width types map to their payload size in bytes.
TYPE_INT8, TYPE_INT16, TYPE_INT32, TYPE_INT64 = 0, 1, 2, 3
TYPE_TRUE, TYPE_FALSE, TYPE_FLOAT, TYPE_DOUBLE = 4, 5, 6, 7
TYPE_DATA, TYPE_NIL, TYPE_OBJECT = 8, 9, 10

_FIXED_WIDTH = {
    TYPE_INT8: 1, TYPE_INT16: 2, TYPE_INT32: 4, TYPE_INT64: 8,
    TYPE_TRUE: 0, TYPE_FALSE: 0, TYPE_FLOAT: 4, TYPE_DOUBLE: 8,
    TYPE_NIL: 0, TYPE_OBJECT: 4,
}

_UNPACK = {
    TYPE_INT8: "<b", TYPE_INT16: "<h", TYPE_INT32: "<i", TYPE_INT64: "<q",
    TYPE_FLOAT: "<f", TYPE_DOUBLE: "<d", TYPE_OBJECT: "<I",
}


@dataclasses.dataclass
class Value:
    key: str
    type: int
    raw: bytes
    decoded: object


@dataclasses.dataclass
class NibObject:
    class_name: str
    value_index: int
    value_count: int


@dataclasses.dataclass
class Archive:
    header: Header
    classes: list
    keys: list
    values: list
    objects: list


# Width in bytes of each element a packed payload can carry, keyed by the tag
# byte that introduces it. The tag reuses the value-type numbering above, so a
# payload led by TYPE_FLOAT holds float32 and one led by TYPE_DOUBLE holds
# float64.
_PACKED_ELEMENT = {TYPE_FLOAT: ("f", 4), TYPE_DOUBLE: ("d", 8)}


def decode_packed_floats(payload):
    """Return the floats a tagged data payload carries, or None.

    A packed payload is one tag byte followed by a whole number of packed
    little-endian floats. Every geometry value in Catch Notes 5.2.8 uses tag
    6 (float32): UIBounds is 17 bytes for four floats, UICenter is 9 bytes for
    two. Tag 7 (float64) is read the same way because both tags come from the
    one value-type table.

    The argument is either the raw bytes of a type-8 value or the mapping
    resolve() emits for one, so a caller working from decoded JSON does not
    have to unhex the payload itself.
    """
    if isinstance(payload, dict):
        text = payload.get("$data_hex")
        if not isinstance(text, str):
            return None
        try:
            payload = bytes.fromhex(text)
        except ValueError:
            return None
    if not isinstance(payload, (bytes, bytearray)) or not payload:
        return None
    element = _PACKED_ELEMENT.get(payload[0])
    if element is None:
        return None
    code, width = element
    body = len(payload) - 1
    if body == 0 or body % width:
        return None
    return struct.unpack_from("<%d%s" % (body // width, code), payload, 1)


def _decode_value_payload(type_tag, raw):
    """Turn a value payload into a Python object, keeping raw bytes elsewhere."""
    if type_tag == TYPE_TRUE:
        return True
    if type_tag == TYPE_FALSE:
        return False
    if type_tag == TYPE_NIL:
        return None
    if type_tag == TYPE_DATA:
        # A type-8 payload is opaque bytes. An earlier version returned str
        # whenever the bytes happened to decode as UTF-8, which gave two
        # different representations to one type and turned packed geometry into
        # control-character mojibake. The bytes stay bytes; represent_data()
        # decides how they are displayed.
        return bytes(raw)
    fmt = _UNPACK.get(type_tag)
    if fmt is None:
        raise NIBFormatError("unknown value type %d" % type_tag)
    return struct.unpack(fmt, raw)[0]


def _is_printable_text(raw):
    """Report whether bytes are UTF-8 text with no control characters."""
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if any(ord(char) < 0x20 or ord(char) == 0x7F for char in text):
        return None
    return text


def represent_data(raw):
    """Describe a type-8 payload as one JSON mapping, the same shape every time.

    The hex of the payload is always present, so nothing decoded here can lose
    a byte. Two structural readings are added when the bytes support them. A
    payload led by a packed-float tag gains "$floats". A payload that is UTF-8
    with no control characters gains "$text". Both tests read the bytes
    themselves, so the same payload always produces the same mapping.
    """
    out = {"$data_hex": raw.hex()}
    floats = decode_packed_floats(raw)
    if floats is not None:
        out["$floats"] = list(floats)
        return out
    text = _is_printable_text(raw)
    if text is not None:
        out["$text"] = text
    return out


def _require(condition, message):
    if not condition:
        raise NIBFormatError(message)


def _read_keys(data, header):
    pos = header.key_offset
    keys = []
    for _ in range(header.key_count):
        length, pos = read_varint(data, pos)
        keys.append(data[pos:pos + length].decode("utf-8", "replace"))
        pos += length
    _require(pos == header.value_offset,
             "key table ended at %d, header declares %d" % (pos, header.value_offset))
    return keys


def _read_classes(data, header):
    pos = header.class_offset
    classes = []
    for _ in range(header.class_count):
        length, pos = read_varint(data, pos)
        extra_count, pos = read_varint(data, pos)
        pos += 4 * extra_count
        classes.append(data[pos:pos + length].decode("utf-8", "replace").rstrip("\0"))
        pos += length
    _require(pos == len(data),
             "class table ended at %d, file is %d bytes" % (pos, len(data)))
    return classes


def _read_values(data, header, keys):
    pos = header.value_offset
    values = []
    for _ in range(header.value_count):
        key_index, pos = read_varint(data, pos)
        type_tag = data[pos]
        pos += 1
        if type_tag == TYPE_DATA:
            length, pos = read_varint(data, pos)
        else:
            length = _FIXED_WIDTH.get(type_tag)
            _require(length is not None, "unknown value type %d" % type_tag)
        raw = data[pos:pos + length]
        _require(len(raw) == length, "value payload ran past the end of the buffer")
        pos += length
        key = keys[key_index] if key_index < len(keys) else "<key %d>" % key_index
        values.append(Value(key, type_tag, raw, _decode_value_payload(type_tag, raw)))
    _require(pos == header.class_offset,
             "value table ended at %d, header declares %d" % (pos, header.class_offset))
    return values


def _read_objects(data, header, classes):
    pos = header.object_offset
    objects = []
    for _ in range(header.object_count):
        class_index, pos = read_varint(data, pos)
        value_index, pos = read_varint(data, pos)
        value_count, pos = read_varint(data, pos)
        name = classes[class_index] if class_index < len(classes) else "<class %d>" % class_index
        objects.append(NibObject(name, value_index, value_count))
    _require(pos == header.key_offset,
             "object table ended at %d, header declares %d" % (pos, header.key_offset))
    return objects


def parse(data):
    """Decode a NIBArchive into its four tables, validating every boundary."""
    header = read_header(data)
    for offset in (header.object_offset, header.key_offset,
                   header.value_offset, header.class_offset):
        _require(0 < offset <= len(data), "table offset %d lies outside the file" % offset)
    classes = _read_classes(data, header)
    keys = _read_keys(data, header)
    values = _read_values(data, header, keys)
    objects = _read_objects(data, header, classes)
    return Archive(header, classes, keys, values, objects)
import json


def resolve(archive):
    """Return one dict per object, carrying every value in the object's window.

    An object's values are an ordered sequence, and one key may appear more than
    once. NSArray names each of its element with the same UINibEncoderEmptyKey,
    so an array of four children encodes that key four times. A JSON object
    cannot hold a repeated key, so **properties** is a list of entries in file
    order, each shaped {"key", "type", "value"}, and **properties_by_key** maps
    each key to the list of entries that carry it. Both views hold the same
    entry objects, and the length of "properties" equals the object's declared
    value count.
    """
    out = []
    for index, obj in enumerate(archive.objects):
        entries = []
        by_key = {}
        window = archive.values[obj.value_index:obj.value_index + obj.value_count]
        for value in window:
            if value.type == TYPE_OBJECT:
                decoded = {"$ref": value.decoded}
            elif value.type == TYPE_DATA:
                decoded = represent_data(value.decoded)
            else:
                decoded = value.decoded
            entry = {"key": value.key, "type": value.type, "value": decoded}
            entries.append(entry)
            by_key.setdefault(value.key, []).append(entry)
        out.append({"index": index, "class": obj.class_name,
                    "properties": entries, "properties_by_key": by_key})
    return out


def to_json(archive):
    """Serialize the resolved graph deterministically."""
    document = {
        "format_version": [archive.header.major, archive.header.minor],
        "counts": {
            "objects": archive.header.object_count,
            "keys": archive.header.key_count,
            "values": archive.header.value_count,
            "classes": archive.header.class_count,
        },
        "classes": archive.classes,
        "objects": resolve(archive),
    }
    return json.dumps(document, indent=2, sort_keys=True)


def main(argv):
    if len(argv) < 2:
        print("usage: python3 -m tools.nibarchive <file.nib> [-o out.json]",
              file=sys.stderr)
        return 2
    with open(argv[1], "rb") as fh:
        text = to_json(parse(fh.read()))
    if "-o" in argv:
        with open(argv[argv.index("-o") + 1], "w") as fh:
            fh.write(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
