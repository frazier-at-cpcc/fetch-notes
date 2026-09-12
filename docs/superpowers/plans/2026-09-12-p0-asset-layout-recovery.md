# P0 Asset and Layout Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the tooling that regenerates every Catch Notes 5.2.8 asset and layout measurement from a hash-verified IPA, without committing a copyrighted byte to a public repository.

**Architecture:** Four independent Python command line tools in `tools/`, each with one responsibility, plus one manual decompilation document. `extract_bundle.py` verifies and unpacks. `nibarchive.py` decodes the NIBArchive container format and knows nothing about UIKit. `nib_layout.py` interprets the decoded graph as view geometry and knows nothing about file formats. `asset_manifest.py` catalogs images and generates an asset catalog. The format layer and the interpretation layer stay separate so that a wrong interpretation never requires touching a verified parser.

**Tech Stack:** Python 3.9 or later, standard library only. `pytest` for tests. Ghidra for Task 7. No third-party runtime dependencies.

**Spec:** `docs/superpowers/specs/2026-09-12-p0-asset-layout-recovery-design.md`

## Global Constraints

- **Standard library only** at run time. The existing `tools/objc_dump32.py` sets this precedent. `pytest` is a development dependency and never an import inside `tools/`.
- **Pinned artifact MD5:** `9a891d439c74198cfa32e39a37e6bb34`. Any tool that reads the IPA verifies this value first.
- **No copyrighted bytes in git.** Everything derived from the bundle lands under `build/`, which `.gitignore` already excludes. Committed outputs are descriptions: manifests, layout reports, and analysis prose.
- **Tests skip rather than fail when `build/Catch.app` is absent.** A fresh clone has no bundle, and the suite must stay green for anyone who has not supplied their own IPA.
- **Deterministic output.** Every JSON writer sorts keys and uses `indent=2`, so reruns produce identical bytes and diffs stay readable.
- **Writing register for committed prose** follows `academic-writing-standards`: no em-dashes, no contractions, active voice.

## Verified format facts

Planning measured these directly. Tasks below assert them, so they are test expectations rather than background.

| Fact | Value |
|---|---|
| NIBArchive magic | bytes `NIBArchive`, offset 0, length 10 |
| Header | ten little-endian `uint32` at offset 10: major, minor, object count, object offset, key count, key offset, value count, value offset, class count, class offset |
| Format version, all 17 files | major 1, minor 9 |
| Varint encoding | 7 bits per byte, little-endian order, the byte with bit `0x80` **set** terminates |
| Value type sizes | `0`=int8/1, `1`=int16/2, `2`=int32/4, `3`=int64/8, `4`=true/0, `5`=false/0, `6`=float/4, `7`=double/8, `8`=data/varint-prefixed, `9`=nil/0, `10`=object ref/4 |
| Table adjacency | objects end at key offset, keys end at value offset, values end at class offset, classes end at file size |
| PNG counts | 546 total, 259 `@2x` pairs, 28 single-resolution |

---

### Task 1: Test scaffolding and hash-verified extraction

**Files:**
- Create: `tools/extract_bundle.py`
- Create: `tests/conftest.py`
- Create: `tests/test_extract_bundle.py`
- Modify: `.gitignore` (confirm `build/` present)

**Interfaces:**
- Consumes: nothing
- Produces: `extract_bundle.verify(path: str, expected_md5: str = EXPECTED_MD5) -> str` returning the computed digest and raising `HashMismatch` otherwise. `extract_bundle.extract(ipa: str, dest: str) -> str` returning the path to the unpacked `.app`. Module constant `EXPECTED_MD5: str`. Exception class `HashMismatch(Exception)`. Test fixture `bundle_dir` yielding a `pathlib.Path` to `build/Catch.app` or skipping.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_extract_bundle.py
import hashlib
import zipfile

import pytest

from tools import extract_bundle


def test_verify_accepts_matching_digest(tmp_path):
    f = tmp_path / "sample.bin"
    f.write_bytes(b"catch")
    digest = hashlib.md5(b"catch").hexdigest()
    assert extract_bundle.verify(str(f), digest) == digest


def test_verify_rejects_mismatched_digest(tmp_path):
    f = tmp_path / "sample.bin"
    f.write_bytes(b"catch")
    with pytest.raises(extract_bundle.HashMismatch) as err:
        extract_bundle.verify(str(f), "0" * 32)
    assert "0" * 32 in str(err.value)


def test_extract_returns_app_directory(tmp_path):
    ipa = tmp_path / "fake.ipa"
    with zipfile.ZipFile(ipa, "w") as z:
        z.writestr("Payload/Catch.app/Info.plist", "<plist/>")
        z.writestr("Payload/Catch.app/icon.png", "notreallyapng")
    dest = tmp_path / "build"
    app = extract_bundle.extract(str(ipa), str(dest))
    assert app.endswith("Payload/Catch.app")
    assert (dest / "Payload" / "Catch.app" / "Info.plist").exists()


def test_expected_md5_is_the_pinned_artifact():
    assert extract_bundle.EXPECTED_MD5 == "9a891d439c74198cfa32e39a37e6bb34"
```

```python
# tests/conftest.py
import pathlib

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def bundle_dir():
    """Path to the unpacked Catch.app, or skip when no one has supplied an IPA."""
    app = REPO_ROOT / "build" / "Payload" / "Catch.app"
    if not app.is_dir():
        pytest.skip(
            "build/Payload/Catch.app is absent. "
            "Run: python3 -m tools.extract_bundle <path-to-Catch.ipa>"
        )
    return app


@pytest.fixture(scope="session")
def nib_paths(bundle_dir):
    paths = sorted(bundle_dir.glob("*.nib")) + sorted(bundle_dir.glob("*.lproj/*.nib"))
    if not paths:
        pytest.skip("no NIB files in the bundle")
    return paths
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_extract_bundle.py -v`
Expected: FAIL, collection error `ModuleNotFoundError: No module named 'tools'`

- [ ] **Step 3: Make `tools` importable and write the implementation**

Create the empty file `tools/__init__.py`, then:

```python
#!/usr/bin/env python3
"""Verify and unpack the archived Catch Notes IPA.

The pinned digest makes the pipeline deterministic. Two contributors who run
this tool either produce byte-identical output or learn immediately that their
artifacts differ.
"""

import hashlib
import os
import sys
import zipfile

EXPECTED_MD5 = "9a891d439c74198cfa32e39a37e6bb34"
ARCHIVE_URL = (
    "https://archive.org/download/CatchiPA/"
    "Catch-E03D11BF-B1E7-4617-A604-D14A48A8559A.ipa"
)


class HashMismatch(Exception):
    """Raised when the supplied IPA is not the pinned artifact."""


def verify(path, expected_md5=EXPECTED_MD5):
    """Return the file's MD5 digest, raising HashMismatch when it differs."""
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    digest = h.hexdigest()
    if digest != expected_md5:
        raise HashMismatch(
            "%s has MD5 %s, expected %s. Obtain the pinned artifact from %s"
            % (path, digest, expected_md5, ARCHIVE_URL)
        )
    return digest


def extract(ipa, dest):
    """Unpack the IPA into dest and return the path to the .app directory."""
    os.makedirs(dest, exist_ok=True)
    with zipfile.ZipFile(ipa) as z:
        names = [n for n in z.namelist() if not n.startswith("/") and ".." not in n]
        z.extractall(dest, members=names)
    payload = os.path.join(dest, "Payload")
    for entry in sorted(os.listdir(payload)):
        if entry.endswith(".app"):
            return os.path.join(payload, entry)
    raise FileNotFoundError("no .app directory inside %s" % payload)


def main(argv):
    if len(argv) < 2:
        print("usage: python3 -m tools.extract_bundle <path-to-Catch.ipa> [dest]",
              file=sys.stderr)
        return 2
    ipa = argv[1]
    dest = argv[2] if len(argv) > 2 else "build"
    print("verifying %s" % ipa)
    verify(ipa)
    app = extract(ipa, dest)
    print("extracted to %s" % app)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_extract_bundle.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add tools/__init__.py tools/extract_bundle.py tests/conftest.py tests/test_extract_bundle.py .gitignore
git commit -m "feat(p0): hash-verified IPA extraction and test scaffolding"
```

---

### Task 2: NIBArchive varint and header

**Files:**
- Create: `tools/nibarchive.py`
- Create: `tests/test_nibarchive.py`

**Interfaces:**
- Consumes: `tests/conftest.py` fixtures `bundle_dir`, `nib_paths` from Task 1
- Produces: `nibarchive.read_varint(data: bytes, pos: int) -> tuple[int, int]` returning `(value, next_pos)`. `nibarchive.Header` dataclass with fields `major, minor, object_count, object_offset, key_count, key_offset, value_count, value_offset, class_count, class_offset`, all `int`. `nibarchive.read_header(data: bytes) -> Header`. `nibarchive.MAGIC: bytes`. Exception `NIBFormatError(Exception)`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_nibarchive.py
import pytest

from tools import nibarchive


def test_varint_single_byte_terminator():
    # 0x81 -> low seven bits 0x01, high bit terminates
    assert nibarchive.read_varint(b"\x81", 0) == (1, 1)


def test_varint_multi_byte_little_endian():
    # 0x00 contributes 0, 0x81 contributes 1 << 7
    assert nibarchive.read_varint(b"\x00\x81", 0) == (128, 2)


def test_varint_respects_start_position():
    assert nibarchive.read_varint(b"\xff\x85", 1) == (5, 2)


def test_rejects_non_nibarchive(tmp_path):
    with pytest.raises(nibarchive.NIBFormatError):
        nibarchive.read_header(b"bplist00" + b"\x00" * 64)


def test_every_nib_reports_version_one_nine(nib_paths):
    for path in nib_paths:
        header = nibarchive.read_header(path.read_bytes())
        assert (header.major, header.minor) == (1, 9), path.name


def test_known_header_counts(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    header = nibarchive.read_header(data)
    assert header.object_count == 15
    assert header.key_count == 22
    assert header.value_count == 39
    assert header.class_count == 5
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_nibarchive.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.nibarchive'`

- [ ] **Step 3: Write the implementation**

```python
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_nibarchive.py -v`
Expected: 6 passed, or 4 passed and 2 skipped when no bundle is present

- [ ] **Step 5: Commit**

```bash
git add tools/nibarchive.py tests/test_nibarchive.py
git commit -m "feat(p0): NIBArchive varint decoding and header parsing"
```

---

### Task 3: NIBArchive table decoding with self-validation

**Files:**
- Modify: `tools/nibarchive.py`
- Modify: `tests/test_nibarchive.py`

**Interfaces:**
- Consumes: `Header`, `read_varint`, `NIBFormatError` from Task 2
- Produces: `nibarchive.Value` dataclass with fields `key: str`, `type: int`, `raw: bytes`, `decoded: object`. `nibarchive.NibObject` dataclass with fields `class_name: str`, `value_index: int`, `value_count: int`. `nibarchive.Archive` dataclass with fields `header: Header`, `classes: list[str]`, `keys: list[str]`, `values: list[Value]`, `objects: list[NibObject]`. `nibarchive.parse(data: bytes) -> Archive`.

The self-validating check the spec requires lives here. Each table must end at exactly the offset the header declares for the next table, and the class table must end at the file size.

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_nibarchive.py

def test_known_keys_and_classes(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    archive = nibarchive.parse(data)
    assert archive.keys[0] == "UIOriginalClassName"
    assert archive.classes == [
        "NSObject",
        "UIProxyObject",
        "NSArray",
        "NSString",
        "UIClassSwapper",
    ]
    assert archive.objects[0].class_name == "NSObject"
    assert archive.objects[0].value_count == 6


def test_value_types_match_measured_histogram(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    archive = nibarchive.parse(data)
    histogram = {}
    for value in archive.values:
        histogram[value.type] = histogram.get(value.type, 0) + 1
    assert histogram == {0: 1, 5: 7, 8: 9, 10: 22}


def test_all_seventeen_nibs_parse_and_self_validate(nib_paths):
    assert len(nib_paths) == 17
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        assert len(archive.objects) == archive.header.object_count, path.name
        assert len(archive.keys) == archive.header.key_count, path.name
        assert len(archive.values) == archive.header.value_count, path.name
        assert len(archive.classes) == archive.header.class_count, path.name


def test_truncated_archive_is_rejected(bundle_dir):
    data = (bundle_dir / "TagViewController.nib").read_bytes()
    with pytest.raises(nibarchive.NIBFormatError):
        nibarchive.parse(data[: len(data) // 2])
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_nibarchive.py -v`
Expected: FAIL with `AttributeError: module 'tools.nibarchive' has no attribute 'parse'`

- [ ] **Step 3: Write the implementation**

Append to `tools/nibarchive.py`:

```python
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


def _decode_value_payload(type_tag, raw):
    """Turn a value payload into a Python object, keeping raw bytes elsewhere."""
    if type_tag == TYPE_TRUE:
        return True
    if type_tag == TYPE_FALSE:
        return False
    if type_tag == TYPE_NIL:
        return None
    if type_tag == TYPE_DATA:
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError:
            return raw
    fmt = _UNPACK.get(type_tag)
    if fmt is None:
        raise NIBFormatError("unknown value type %d" % type_tag)
    return struct.unpack(fmt, raw)[0]


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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_nibarchive.py -v`
Expected: 10 passed

- [ ] **Step 5: Commit**

```bash
git add tools/nibarchive.py tests/test_nibarchive.py
git commit -m "feat(p0): decode NIBArchive tables with boundary self-validation"
```

---

### Task 4: Object graph resolution, JSON output, and command line interface

**Files:**
- Modify: `tools/nibarchive.py`
- Modify: `tests/test_nibarchive.py`
- Create: `tests/fixtures/CatchToolbarNavigationController.graph.json`

**Interfaces:**
- Consumes: `Archive`, `parse` from Task 3
- Produces: `nibarchive.resolve(archive: Archive) -> list[dict]` returning one dict per object, shaped `{"index": int, "class": str, "properties": {key: {"type": int, "value": object}}}`, where a value of type 10 becomes `{"$ref": int}`. `nibarchive.to_json(archive: Archive) -> str`. A `__main__` entry point accepting a NIB path and an optional `-o` output path.

- [ ] **Step 1: Write the failing tests**

```python
# append to tests/test_nibarchive.py
import json
import pathlib

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def test_resolve_shapes_objects_with_named_properties(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    assert len(objects) == 15
    first = objects[0]
    assert first["index"] == 0
    assert first["class"] == "NSObject"
    assert len(first["properties"]) == 6


def test_object_references_become_ref_markers(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    refs = [
        prop["value"]
        for obj in objects
        for prop in obj["properties"].values()
        if prop["type"] == nibarchive.TYPE_OBJECT
    ]
    assert refs, "expected at least one object reference"
    assert all(set(ref.keys()) == {"$ref"} for ref in refs)


def test_graph_matches_golden_fixture(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    produced = json.loads(nibarchive.to_json(nibarchive.parse(data)))
    expected = json.loads((FIXTURES / "CatchToolbarNavigationController.graph.json").read_text())
    assert produced == expected
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_nibarchive.py -v`
Expected: FAIL with `AttributeError: module 'tools.nibarchive' has no attribute 'resolve'`

- [ ] **Step 3: Write the implementation**

Append to `tools/nibarchive.py`:

```python
import json


def resolve(archive):
    """Return one dict per object, with values named by their key strings."""
    out = []
    for index, obj in enumerate(archive.objects):
        properties = {}
        window = archive.values[obj.value_index:obj.value_index + obj.value_count]
        for value in window:
            if value.type == TYPE_OBJECT:
                decoded = {"$ref": value.decoded}
            elif isinstance(value.decoded, bytes):
                decoded = {"$data_hex": value.decoded.hex()}
            else:
                decoded = value.decoded
            properties[value.key] = {"type": value.type, "value": decoded}
        out.append({"index": index, "class": obj.class_name, "properties": properties})
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
```

- [ ] **Step 4: Generate the golden fixture, then read it before trusting it**

```bash
mkdir -p tests/fixtures
python3 -m tools.nibarchive build/Payload/Catch.app/CatchToolbarNavigationController.nib \
  -o tests/fixtures/CatchToolbarNavigationController.graph.json
```

Open the file. Confirm that `counts` reads `{"classes": 5, "keys": 22, "objects": 15, "values": 39}`, that `classes` lists the five expected names, and that no property value contains raw image bytes. A fixture generated by the code it tests proves only stability, so this manual read is the step that makes it meaningful.

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python3 -m pytest tests/ -v`
Expected: 17 passed

- [ ] **Step 6: Commit**

```bash
git add tools/nibarchive.py tests/test_nibarchive.py tests/fixtures/
git commit -m "feat(p0): resolve NIB object graph to deterministic JSON"
```

---

### Task 5: Layout reporter

**Files:**
- Create: `tools/nib_layout.py`
- Create: `tests/test_nib_layout.py`

**Interfaces:**
- Consumes: `nibarchive.parse`, `nibarchive.resolve` from Tasks 3 and 4
- Produces: `nib_layout.build_tree(objects: list[dict]) -> list[dict]` returning root nodes, each `{"index": int, "class": str, "frame": dict | None, "raw": dict, "children": list}`. `nib_layout.parse_rect(text: str) -> dict | None` turning `"{{0, 0}, {320, 44}}"` into `{"x": 0.0, "y": 0.0, "width": 320.0, "height": 44.0}`. `nib_layout.render_markdown(name: str, roots: list[dict]) -> str`.

The spec requires that every interpretation print the raw decoded value beside it. `build_tree` therefore carries a `raw` dict on every node holding the untouched properties.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_nib_layout.py
from tools import nib_layout, nibarchive


def test_parse_rect_reads_cgrect_strings():
    assert nib_layout.parse_rect("{{0, 0}, {320, 44}}") == {
        "x": 0.0, "y": 0.0, "width": 320.0, "height": 44.0,
    }


def test_parse_rect_accepts_floats_and_negatives():
    assert nib_layout.parse_rect("{{-1.5, 2}, {320.25, 44}}") == {
        "x": -1.5, "y": 2.0, "width": 320.25, "height": 44.0,
    }


def test_parse_rect_returns_none_for_non_rect():
    assert nib_layout.parse_rect("UIView") is None
    assert nib_layout.parse_rect("") is None


def test_every_node_carries_its_raw_properties():
    objects = [
        {"index": 0, "class": "UIView",
         "properties": {"UIBounds": {"type": 8, "value": "{{0, 0}, {320, 44}}"}}},
    ]
    roots = nib_layout.build_tree(objects)
    assert roots[0]["raw"] == objects[0]["properties"]
    assert roots[0]["frame"] == {"x": 0.0, "y": 0.0, "width": 320.0, "height": 44.0}


def test_subviews_become_children():
    objects = [
        {"index": 0, "class": "UIView",
         "properties": {"UISubviews": {"type": 10, "value": {"$ref": 1}}}},
        {"index": 1, "class": "NSArray",
         "properties": {"UINibEncoderEmptyKey": {"type": 10, "value": {"$ref": 2}}}},
        {"index": 2, "class": "UILabel", "properties": {}},
    ]
    roots = nib_layout.build_tree(objects)
    assert len(roots) == 1
    assert roots[0]["children"][0]["class"] == "UILabel"


def test_all_seventeen_nibs_render_without_raising(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        roots = nib_layout.build_tree(nibarchive.resolve(archive))
        text = nib_layout.render_markdown(path.stem, roots)
        assert text.startswith("# %s" % path.stem), path.name
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_nib_layout.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.nib_layout'`

- [ ] **Step 3: Write the implementation**

```python
#!/usr/bin/env python3
"""Interpret a decoded NIB object graph as view geometry.

Interpretation carries risk, because value semantics differ between UIKit
classes. Every node therefore carries its untouched properties under "raw", so
a reader who disagrees with an interpretation inspects the underlying value
without rerunning the parser.
"""

import re
import sys

from tools import nibarchive

_RECT = re.compile(
    r"^\{\{\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\}\s*,\s*\{\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)\s*\}\}$"
)

# Keys whose value names a child or a collection of children.
_CHILD_KEYS = ("UISubviews", "UINibEncoderEmptyKey", "NSInlinedValue")


def parse_rect(text):
    """Turn a CGRect string into a dict, or return None when it is not one."""
    if not isinstance(text, str):
        return None
    match = _RECT.match(text.strip())
    if not match:
        return None
    x, y, width, height = (float(g) for g in match.groups())
    return {"x": x, "y": y, "width": width, "height": height}


def _refs(properties, keys=_CHILD_KEYS):
    """Yield object indices referenced by any of the given property keys."""
    for key in keys:
        prop = properties.get(key)
        if prop and isinstance(prop.get("value"), dict) and "$ref" in prop["value"]:
            yield prop["value"]["$ref"]


def build_tree(objects):
    """Assemble root nodes with children resolved through subview references."""
    by_index = {obj["index"]: obj for obj in objects}
    nodes = {}
    for obj in objects:
        props = obj["properties"]
        bounds = props.get("UIBounds") or props.get("UIFrame")
        nodes[obj["index"]] = {
            "index": obj["index"],
            "class": obj["class"],
            "frame": parse_rect(bounds["value"]) if bounds else None,
            "raw": props,
            "children": [],
        }

    claimed = set()
    for obj in objects:
        for ref in _refs(obj["properties"]):
            child = by_index.get(ref)
            if child is None:
                continue
            if child["class"] in ("NSArray", "NSMutableArray"):
                for inner in _refs(child["properties"]):
                    if inner in nodes and inner != obj["index"]:
                        nodes[obj["index"]]["children"].append(nodes[inner])
                        claimed.add(inner)
                claimed.add(ref)
            elif ref != obj["index"]:
                nodes[obj["index"]]["children"].append(nodes[ref])
                claimed.add(ref)

    return [node for index, node in sorted(nodes.items()) if index not in claimed]


def _render_node(node, depth, lines):
    indent = "  " * depth
    frame = node["frame"]
    geometry = (
        " frame=(%g, %g, %g, %g)" % (frame["x"], frame["y"], frame["width"], frame["height"])
        if frame else ""
    )
    lines.append("%s- **%s** (object %d)%s" % (indent, node["class"], node["index"], geometry))
    for key in sorted(node["raw"]):
        prop = node["raw"][key]
        lines.append("%s  - `%s` (type %d): `%r`" % (indent, key, prop["type"], prop["value"]))
    for child in node["children"]:
        _render_node(child, depth + 1, lines)


def render_markdown(name, roots):
    """Produce the committed layout report for one NIB."""
    lines = [
        "# %s" % name,
        "",
        "Recovered layout for `%s.nib`. Every interpreted value appears beside the" % name,
        "raw decoded value, so a disputed reading stays auditable.",
        "",
    ]
    for root in roots:
        _render_node(root, 0, lines)
        lines.append("")
    return "\n".join(lines)


def main(argv):
    if len(argv) < 2:
        print("usage: python3 -m tools.nib_layout <file.nib> [-o out.md]", file=sys.stderr)
        return 2
    import os
    with open(argv[1], "rb") as fh:
        archive = nibarchive.parse(fh.read())
    roots = build_tree(nibarchive.resolve(archive))
    text = render_markdown(os.path.basename(argv[1]).replace(".nib", ""), roots)
    if "-o" in argv:
        with open(argv[argv.index("-o") + 1], "w") as fh:
            fh.write(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/ -v`
Expected: 23 passed

- [ ] **Step 5: Commit**

```bash
git add tools/nib_layout.py tests/test_nib_layout.py
git commit -m "feat(p0): render NIB layout reports with raw values beside interpretations"
```

---

### Task 6: Asset manifest and generated asset catalog

**Files:**
- Create: `tools/asset_manifest.py`
- Create: `tests/test_asset_manifest.py`

**Interfaces:**
- Consumes: nothing from earlier tasks
- Produces: `asset_manifest.png_size(path) -> tuple[int, int]` reading width and height from the IHDR chunk. `asset_manifest.split_scale(name: str) -> tuple[str, int]` turning `"icon@2x.png"` into `("icon", 2)`. `asset_manifest.build(bundle: str) -> dict`. `asset_manifest.write_xcassets(manifest: dict, bundle: str, dest: str) -> None`.

Reading IHDR directly avoids a Pillow dependency, which the standard-library-only constraint forbids. A PNG carries an 8-byte signature, then a chunk length and the `IHDR` tag, placing width at offset 16 and height at offset 20, both big-endian `uint32`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_asset_manifest.py
import json
import struct

from tools import asset_manifest


def _png(tmp_path, name, width, height):
    ihdr = struct.pack(">II", width, height) + b"\x08\x06\x00\x00\x00"
    data = (b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + ihdr
            + b"\x00\x00\x00\x00")
    path = tmp_path / name
    path.write_bytes(data)
    return path


def test_png_size_reads_ihdr(tmp_path):
    assert asset_manifest.png_size(_png(tmp_path, "a.png", 320, 44)) == (320, 44)


def test_split_scale_separates_retina_suffix():
    assert asset_manifest.split_scale("icon@2x.png") == ("icon", 2)
    assert asset_manifest.split_scale("icon.png") == ("icon", 1)


def test_build_pairs_retina_variants(tmp_path):
    _png(tmp_path, "icon.png", 10, 10)
    _png(tmp_path, "icon@2x.png", 20, 20)
    _png(tmp_path, "lonely.png", 5, 5)
    manifest = asset_manifest.build(str(tmp_path))
    assert manifest["counts"]["png_total"] == 3
    assert manifest["counts"]["paired"] == 1
    assert manifest["counts"]["single_resolution"] == 1
    icon = manifest["images"]["icon"]
    assert icon["scales"]["1"]["width"] == 10
    assert icon["scales"]["2"]["width"] == 20
    assert len(icon["scales"]["1"]["sha256"]) == 64


def test_manifest_is_deterministic(tmp_path):
    _png(tmp_path, "icon.png", 10, 10)
    first = json.dumps(asset_manifest.build(str(tmp_path)), sort_keys=True)
    second = json.dumps(asset_manifest.build(str(tmp_path)), sort_keys=True)
    assert first == second


def test_xcassets_writes_contents_json(tmp_path):
    _png(tmp_path, "icon.png", 10, 10)
    _png(tmp_path, "icon@2x.png", 20, 20)
    manifest = asset_manifest.build(str(tmp_path))
    dest = tmp_path / "out.xcassets"
    asset_manifest.write_xcassets(manifest, str(tmp_path), str(dest))
    contents = json.loads((dest / "icon.imageset" / "Contents.json").read_text())
    scales = sorted(entry["scale"] for entry in contents["images"])
    assert scales == ["1x", "2x"]
    assert (dest / "icon.imageset" / "icon@2x.png").exists()


def test_real_bundle_matches_measured_counts(bundle_dir):
    manifest = asset_manifest.build(str(bundle_dir))
    assert manifest["counts"]["png_total"] == 546
    assert manifest["counts"]["paired"] == 259
    assert manifest["counts"]["single_resolution"] == 28
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python3 -m pytest tests/test_asset_manifest.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'tools.asset_manifest'`

- [ ] **Step 3: Write the implementation**

```python
#!/usr/bin/env python3
"""Catalog the bundle's assets and generate an Xcode asset catalog.

The manifest is committed and the catalog is not. A reader compares digests and
confirms that a generated catalog matches the archived original, while the
repository never stores the images themselves.
"""

import hashlib
import json
import os
import shutil
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
OTHER_RESOURCE_SUFFIXES = (".ttf", ".css", ".js", ".strings")


def png_size(path):
    """Return (width, height) from the IHDR chunk without decoding pixels."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != PNG_SIGNATURE or head[12:16] != b"IHDR":
        raise ValueError("%s is not a PNG" % path)
    return struct.unpack(">II", head[16:24])


def split_scale(name):
    """Return (base_name, scale) for a possibly retina-suffixed file name."""
    stem = name[:-4] if name.endswith(".png") else name
    if stem.endswith("@2x"):
        return stem[:-3], 2
    if stem.endswith("@3x"):
        return stem[:-3], 3
    return stem, 1


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build(bundle):
    """Walk the bundle and return the manifest document."""
    images = {}
    others = {}
    for name in sorted(os.listdir(bundle)):
        path = os.path.join(bundle, name)
        if not os.path.isfile(path):
            continue
        if name.endswith(".png"):
            base, scale = split_scale(name)
            width, height = png_size(path)
            entry = images.setdefault(base, {"scales": {}})
            entry["scales"][str(scale)] = {
                "file": name,
                "width": width,
                "height": height,
                "bytes": os.path.getsize(path),
                "sha256": _sha256(path),
            }
        elif name.endswith(OTHER_RESOURCE_SUFFIXES):
            others[name] = {"bytes": os.path.getsize(path), "sha256": _sha256(path)}

    png_total = sum(len(entry["scales"]) for entry in images.values())
    paired = sum(1 for entry in images.values() if len(entry["scales"]) > 1)
    single = sum(1 for entry in images.values() if len(entry["scales"]) == 1)
    return {
        "source": {
            "artifact": "Catch Notes 5.2.8",
            "ipa_md5": "9a891d439c74198cfa32e39a37e6bb34",
        },
        "counts": {
            "png_total": png_total,
            "image_sets": len(images),
            "paired": paired,
            "single_resolution": single,
        },
        "images": images,
        "other_resources": others,
    }


def write_xcassets(manifest, bundle, dest):
    """Generate an asset catalog into dest. Never call this on a tracked path."""
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "Contents.json"), "w") as fh:
        json.dump({"info": {"author": "xcode", "version": 1}}, fh, indent=2)
    for base, entry in sorted(manifest["images"].items()):
        imageset = os.path.join(dest, "%s.imageset" % base)
        os.makedirs(imageset, exist_ok=True)
        entries = []
        for scale in sorted(entry["scales"]):
            filename = entry["scales"][scale]["file"]
            shutil.copy2(os.path.join(bundle, filename), os.path.join(imageset, filename))
            entries.append({"idiom": "universal", "filename": filename,
                            "scale": "%sx" % scale})
        with open(os.path.join(imageset, "Contents.json"), "w") as fh:
            json.dump({"images": entries, "info": {"author": "xcode", "version": 1}},
                      fh, indent=2, sort_keys=True)


def main(argv):
    if len(argv) < 2:
        print("usage: python3 -m tools.asset_manifest <Catch.app> "
              "[-m manifest.json] [-x out.xcassets]", file=sys.stderr)
        return 2
    bundle = argv[1]
    manifest = build(bundle)
    if "-m" in argv:
        with open(argv[argv.index("-m") + 1], "w") as fh:
            json.dump(manifest, fh, indent=2, sort_keys=True)
            fh.write("\n")
    if "-x" in argv:
        write_xcassets(manifest, bundle, argv[argv.index("-x") + 1])
    print("%(png_total)d PNG files across %(image_sets)d image sets, "
          "%(paired)d paired, %(single_resolution)d single-resolution" % manifest["counts"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python3 -m pytest tests/ -v`
Expected: 29 passed

- [ ] **Step 5: Commit**

```bash
git add tools/asset_manifest.py tests/test_asset_manifest.py
git commit -m "feat(p0): asset manifest and generated xcassets catalog"
```

---

### Task 7: Capture wheel geometry analysis

**Files:**
- Create: `research/piemenu-geometry.md`

**Interfaces:**
- Consumes: `build/Payload/Catch.app/Catch` and the headers produced by `tools/objc_dump32.py`
- Produces: a prose document. No code and no tests, because the deliverable is recovered constants rather than behavior.

This task is manual analysis in Ghidra. It has no test cycle, so it ends at review rather than at a passing suite.

- [ ] **Step 1: Regenerate the headers and locate the target methods**

```bash
python3 tools/objc_dump32.py build/Payload/Catch.app/Catch --headers build/headers
grep -E 'pathForSliceSegment|layoutIconViews|pathAnimationWithDuration' build/headers/PieMenu.h
```

- [ ] **Step 2: Import the binary into Ghidra**

Create a new non-shared project. Import `build/Payload/Catch.app/Catch`, choosing ARM v7 little endian as the language. Run auto-analysis with the Objective-C analyzers enabled, which names methods from the metadata rather than leaving `FUN_` labels.

- [ ] **Step 3: Recover the slice geometry**

Decompile `+[PieMenu pathForSliceSegment:withCenterPoint:radius:]`. Record the start angle, the sweep per slice, the slice count, and the inner and outer radii. The method builds a `UIBezierPath`, so the arc calls carry the angles as literal float constants or as constants folded into arithmetic.

- [ ] **Step 4: Recover the icon placement**

Decompile `-[PieMenu layoutIconViewsWithRadius:iconScale:]`. Record the icon placement radius as a proportion of the wheel radius, the icon scale factor, and the angular offset that centers an icon inside its slice.

- [ ] **Step 5: Recover the animation**

Decompile `+[PieMenu pathAnimationWithDuration:timingFunctionName:fromPath:toPath:]`. Record the duration and the named `CAMediaTimingFunction`. Then inspect the `_sprungOpen` and `_osSupportsInteractionDuringAnimation` instance variables to record the spring behavior and the rule governing interaction during animation.

- [ ] **Step 6: Write the document**

Write `research/piemenu-geometry.md` with one section per method. State every recovered value in a table with three columns: the constant, the value, and whether the analysis read it directly or estimated it. The spec requires that estimated values stay labeled, because the project treats deviation from the original as a documented defect rather than a silent choice. Follow the `academic-writing-standards` register: no em-dashes, no contractions, active voice.

- [ ] **Step 7: Commit**

```bash
git add research/piemenu-geometry.md
git commit -m "docs(p0): recover PieMenu capture wheel geometry from armv7 binary"
```

---

### Task 8: Run the pipeline and commit the derived outputs

**Files:**
- Create: `research/asset-manifest.json`
- Create: `research/nib-layouts/*.md` and `research/nib-layouts/*.json` (17 of each)
- Create: `tools/run_p0.sh`
- Modify: `README.md`

**Interfaces:**
- Consumes: every tool from Tasks 1 through 6
- Produces: the committed derived artifacts, and one script that regenerates them

- [ ] **Step 1: Write the pipeline script**

```bash
#!/usr/bin/env bash
# tools/run_p0.sh: regenerate every P0 output from a verified IPA.
# Usage: tools/run_p0.sh path/to/Catch.ipa
set -euo pipefail

IPA="${1:?usage: tools/run_p0.sh <path-to-Catch.ipa>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 -m tools.extract_bundle "$IPA" build
APP="build/Payload/Catch.app"

mkdir -p research/nib-layouts
for nib in "$APP"/*.nib "$APP"/*.lproj/*.nib; do
  [ -e "$nib" ] || continue
  name="$(basename "$nib" .nib)"
  python3 -m tools.nibarchive "$nib" -o "research/nib-layouts/${name}.json"
  python3 -m tools.nib_layout "$nib" -o "research/nib-layouts/${name}.md"
done

python3 -m tools.asset_manifest "$APP" \
  -m research/asset-manifest.json \
  -x build/Catch.xcassets

python3 tools/objc_dump32.py "$APP/Catch" --headers build/headers

echo "P0 complete. Committed outputs are under research/. Everything under build/ stays local."
```

- [ ] **Step 2: Run it**

```bash
chmod +x tools/run_p0.sh
tools/run_p0.sh ~/Downloads/Catch.ipa
```

Expected: 17 JSON files and 17 markdown files under `research/nib-layouts/`, one `research/asset-manifest.json`, and a `build/Catch.xcassets` that git ignores.

- [ ] **Step 3: Confirm no copyrighted bytes entered the index**

```bash
git add -A
git status --short
git diff --cached --name-only | grep -E '\.(png|ttf|css|js|strings|ipa)$' && {
  echo "FAIL: copyrighted asset staged"; exit 1; } || echo "clean"
```

Expected: `clean`. A non-empty grep means `.gitignore` needs repair before committing.

- [ ] **Step 4: Verify the manifest counts against the measured values**

```bash
python3 -c "
import json
m = json.load(open('research/asset-manifest.json'))
c = m['counts']
assert c['png_total'] == 546, c
assert c['paired'] == 259, c
assert c['single_resolution'] == 28, c
print('manifest matches measured counts')
"
```

Expected: `manifest matches measured counts`

- [ ] **Step 5: Report which view controllers ship no NIB**

The spec records that the bundle holds 17 NIB files while the class dump names
far more view controllers, and it requires P0 to report that gap so P3 knows
which layouts need decompilation instead of extraction.

```bash
python3 - <<'EOF' > research/nib-coverage.md
import os, re
headers = sorted(os.listdir("build/headers"))
controllers = sorted(h[:-2] for h in headers if h.endswith("ViewController.h"))
nibs = set()
for root, _dirs, files in os.walk("build/Payload/Catch.app"):
    nibs.update(f[:-4] for f in files if f.endswith(".nib"))
missing = [c for c in controllers if not any(n.startswith(c) for n in nibs)]
print("# NIB Coverage\n")
print("The bundle ships %d NIB files for %d view controller classes." % (len(nibs), len(controllers)))
print("P3 recovers the following %d layouts by decompilation, because no NIB\ndescribes them.\n" % len(missing))
for name in missing:
    print("- `%s`" % name)
EOF
```

Read the generated file before committing it. Confirm the controller count is
plausible against `build/headers` and that the list names real classes.

- [ ] **Step 6: Add the README**

Write `README.md` covering what the repository holds, the three-line quick start (`pip install pytest`, `tools/run_p0.sh <ipa>`, `python3 -m pytest`), the rule that no copyrighted byte is committed, and a pointer to the teardown and the P0 spec. Follow the `academic-writing-standards` register.

The README also records the open licensing question the spec raises: `jr_hand.ttf` is third-party, its redistribution terms are unknown, and P3 must resolve them before shipping the original typography.

- [ ] **Step 7: Run the full suite one final time**

Run: `python3 -m pytest tests/ -v`
Expected: 26 passed

- [ ] **Step 8: Commit**

```bash
git add research/ tools/run_p0.sh README.md
git commit -m "feat(p0): regenerate and commit derived layout and asset outputs"
```

---

## Completion criteria

P0 is done when all of the following hold.

1. `python3 -m pytest tests/ -v` reports 29 passed with a bundle present. On a clean clone with no bundle, the 8 tests that need one skip and the remaining 21 pass.
2. `research/nib-layouts/` holds 17 markdown reports and 17 JSON graphs.
3. `research/asset-manifest.json` reports 546 PNG files, 259 paired, 28 single-resolution.
4. `research/piemenu-geometry.md` states every recovered constant and labels every estimate.
5. `git ls-files` lists no file with a `.png`, `.ttf`, `.css`, `.js`, `.strings`, or `.ipa` extension.
6. `research/nib-coverage.md` names every view controller that ships no NIB.
7. `README.md` records the `jr_hand.ttf` licensing question as unresolved.
8. `tools/run_p0.sh` regenerates every output from a bare clone plus an IPA.
