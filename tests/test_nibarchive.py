import pytest
import struct

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
import json
import pathlib

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def test_resolve_shapes_objects_with_ordered_properties(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    assert len(objects) == 15
    first = objects[0]
    assert first["index"] == 0
    assert first["class"] == "NSObject"
    assert len(first["properties"]) == 6
    assert all(set(entry) == {"key", "type", "value"} for entry in first["properties"])


def test_properties_by_key_indexes_the_same_entries(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    for obj in nibarchive.resolve(nibarchive.parse(data)):
        indexed = [entry for entries in obj["properties_by_key"].values() for entry in entries]
        assert len(indexed) == len(obj["properties"])
        for key, entries in obj["properties_by_key"].items():
            assert [entry["key"] for entry in entries] == [key] * len(entries)
            assert entries == [entry for entry in obj["properties"] if entry["key"] == key]


def test_object_references_become_ref_markers(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    refs = [
        entry["value"]
        for obj in objects
        for entry in obj["properties"]
        if entry["type"] == nibarchive.TYPE_OBJECT
    ]
    assert refs, "expected at least one object reference"
    assert all(set(ref.keys()) == {"$ref"} for ref in refs)


def test_graph_matches_golden_fixture(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    produced = json.loads(nibarchive.to_json(nibarchive.parse(data)))
    expected = json.loads((FIXTURES / "CatchToolbarNavigationController.graph.json").read_text())
    assert produced == expected
# Repeated keys inside one object's value window. A NIB object's values are an
# ordered sequence, and NSArray names each of its elements with the same
# UINibEncoderEmptyKey. A by-key dict cannot hold them all.


def test_resolve_emits_every_declared_value(nib_paths):
    # The invariant whose absence let 620 of 4229 values ship discarded: the
    # object windows tile the value table, so the emitted entries must number
    # exactly what the header declares.
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        emitted = sum(len(obj["properties"]) for obj in nibarchive.resolve(archive))
        assert emitted == archive.header.value_count, path.name


def test_repeated_keys_survive_in_file_order(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    array = objects[4]
    assert array["class"] == "NSArray"
    refs = [
        entry["value"]["$ref"]
        for entry in array["properties"]
        if entry["key"] == "UINibEncoderEmptyKey"
    ]
    assert refs == [6, 5, 7, 3]
    indexed = [
        entry["value"]["$ref"]
        for entry in array["properties_by_key"]["UINibEncoderEmptyKey"]
    ]
    assert indexed == [6, 5, 7, 3]


def test_every_array_element_reaches_the_layout_tree(bundle_dir):
    # Lives here rather than in tests/test_nib_layout.py because it pins the
    # contract between resolve() and build_tree(), which is what the dropped
    # values broke.
    from tools import nib_layout

    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    roots = nib_layout.build_tree(nibarchive.resolve(nibarchive.parse(data)))
    array = next(node for node in roots if node["index"] == 4)
    assert [child["index"] for child in array["children"]] == [6, 5, 7, 3]
# Type-8 representation. A data payload is opaque bytes, so it reaches JSON as
# one mapping shape whatever the bytes happen to hold.


def test_data_values_decode_to_bytes(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        for value in archive.values:
            if value.type == nibarchive.TYPE_DATA:
                assert isinstance(value.decoded, bytes), (path.name, value.key)


def test_data_representation_is_one_shape_and_keeps_every_byte(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        raws = [v.raw for v in archive.values if v.type == nibarchive.TYPE_DATA]
        emitted = [
            entry["value"]
            for obj in nibarchive.resolve(archive)
            for entry in obj["properties"]
            if entry["type"] == nibarchive.TYPE_DATA
        ]
        assert len(emitted) == len(raws), path.name
        for raw, value in zip(raws, emitted):
            assert isinstance(value, dict), path.name
            assert bytes.fromhex(value["$data_hex"]) == raw, path.name
            assert not ("$floats" in value and "$text" in value), path.name


def test_packed_geometry_reaches_json_as_floats(bundle_dir):
    # PadNoteViewController holds a view sized 768 by 960 centred at
    # (384, 524), which is the full iPad canvas under a 44 point toolbar.
    data = (bundle_dir / "PadNoteViewController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    bounds = [
        entry["value"]["$floats"]
        for obj in objects
        for entry in obj["properties"]
        if entry["key"] == "UIBounds"
    ]
    centers = [
        entry["value"]["$floats"]
        for obj in objects
        for entry in obj["properties"]
        if entry["key"] == "UICenter"
    ]
    assert [0.0, 0.0, 768.0, 960.0] in bounds
    assert [384.0, 524.0] in centers


def test_every_bounds_and_center_is_a_packed_float_vector(nib_paths):
    # Measured across the 17 NIBs: 120 UIBounds of four floats and 120
    # UICenter of two, every one led by tag 6.
    widths = {}
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        for value in archive.values:
            if value.key not in ("UIBounds", "UICenter"):
                continue
            assert value.type == nibarchive.TYPE_DATA, path.name
            assert value.raw[0] == nibarchive.TYPE_FLOAT, path.name
            floats = nibarchive.decode_packed_floats(value.raw)
            assert floats is not None, (path.name, value.key)
            widths.setdefault(value.key, []).append(len(floats))
    assert len(widths["UIBounds"]) == 120
    assert len(widths["UICenter"]) == 120
    assert set(widths["UIBounds"]) == {4}
    assert set(widths["UICenter"]) == {2}


def test_decode_packed_floats_reads_a_resolved_mapping():
    raw = b"\x06" + struct.pack("<4f", 0.0, 0.0, 320.0, 44.0)
    mapping = nibarchive.represent_data(raw)
    assert mapping["$floats"] == [0.0, 0.0, 320.0, 44.0]
    assert nibarchive.decode_packed_floats(mapping) == (0.0, 0.0, 320.0, 44.0)


def test_decode_packed_floats_refuses_payloads_that_are_not_vectors():
    assert nibarchive.decode_packed_floats(b"") is None
    assert nibarchive.decode_packed_floats(b"0.132 0.129 0.129") is None
    assert nibarchive.decode_packed_floats(b"\x06\x00\x00") is None
    assert nibarchive.decode_packed_floats(b"\x06") is None
    assert nibarchive.decode_packed_floats({"$data_hex": "zz"}) is None
    assert nibarchive.decode_packed_floats(None) is None


def test_text_payloads_keep_their_text(bundle_dir):
    data = (bundle_dir / "CatchToolbarNavigationController.nib").read_bytes()
    objects = nibarchive.resolve(nibarchive.parse(data))
    texts = [
        entry["value"]["$text"]
        for obj in objects
        for entry in obj["properties"]
        if entry["key"] == "NS.bytes"
    ]
    assert "CatchToolbarNavigationController" in texts
