from tools import nib_layout, nibarchive


def _obj(index, class_name, *pairs):
    """Build one resolved object in the shape tools/nibarchive.py emits.

    A resolved object carries its values as an ordered list, because one key
    repeats inside a single object. Each pair is (key, type, value).
    """
    properties = [{"key": key, "type": type_tag, "value": value}
                  for key, type_tag, value in pairs]
    by_key = {}
    for entry in properties:
        by_key.setdefault(entry["key"], []).append(entry)
    return {"index": index, "class": class_name,
            "properties": properties, "properties_by_key": by_key}


# The archive stores geometry as two type-8 payloads, each a tag byte 6
# followed by packed little-endian float32 values. These two come from
# PadNoteViewController.nib, object 16.
_BOUNDS_HEX = "0600000000000000000000404400007044"   # (0, 0, 768, 960)
_CENTER_HEX = "060000c04300000344"                   # (384, 524)


# --------------------------------------------------------------------------
# Geometry


def test_parse_bounds_reads_four_packed_floats():
    assert nib_layout.parse_bounds({"$data_hex": _BOUNDS_HEX}) == {
        "x": 0.0, "y": 0.0, "width": 768.0, "height": 960.0,
    }


def test_parse_center_reads_two_packed_floats():
    assert nib_layout.parse_center({"$data_hex": _CENTER_HEX}) == {
        "x": 384.0, "y": 524.0,
    }


def test_parse_bounds_refuses_a_two_float_payload():
    assert nib_layout.parse_bounds({"$data_hex": _CENTER_HEX}) is None


def test_parse_center_refuses_a_four_float_payload():
    assert nib_layout.parse_center({"$data_hex": _BOUNDS_HEX}) is None


def test_geometry_parsers_refuse_values_that_are_not_payloads():
    for value in (None, "UIView", "", {"$text": "UIView"}, {"$data_hex": "zz"}):
        assert nib_layout.parse_bounds(value) is None
        assert nib_layout.parse_center(value) is None


def test_the_frame_is_the_center_less_half_the_size():
    bounds = nib_layout.parse_bounds({"$data_hex": _BOUNDS_HEX})
    center = nib_layout.parse_center({"$data_hex": _CENTER_HEX})
    # A view 768 by 960 centered at (384, 524) sits below a 44 point toolbar.
    assert nib_layout.compute_frame(bounds, center) == {
        "x": 0.0, "y": 44.0, "width": 768.0, "height": 960.0,
    }


def test_compute_frame_needs_both_halves_of_the_encoding():
    bounds = nib_layout.parse_bounds({"$data_hex": _BOUNDS_HEX})
    center = nib_layout.parse_center({"$data_hex": _CENTER_HEX})
    assert nib_layout.compute_frame(bounds, None) is None
    assert nib_layout.compute_frame(None, center) is None


def test_a_node_reports_the_frame_beside_both_source_values():
    objects = [_obj(0, "UIView",
                    ("UIBounds", 8, {"$data_hex": _BOUNDS_HEX}),
                    ("UICenter", 8, {"$data_hex": _CENTER_HEX}))]
    node = nib_layout.build_tree(objects)[0]
    assert node["frame"] == {"x": 0.0, "y": 44.0, "width": 768.0, "height": 960.0}
    assert node["bounds"] == {"x": 0.0, "y": 0.0, "width": 768.0, "height": 960.0}
    assert node["center"] == {"x": 384.0, "y": 524.0}


# --------------------------------------------------------------------------
# Raw values


def test_every_node_carries_its_raw_properties_in_file_order():
    objects = [_obj(0, "NSArray",
                    ("UINibEncoderEmptyKey", 10, {"$ref": 1}),
                    ("UINibEncoderEmptyKey", 10, {"$ref": 2}))]
    node = nib_layout.build_tree(objects)[0]
    assert node["raw"] == objects[0]["properties"]
    assert [entry["value"]["$ref"] for entry in node["raw"]] == [1, 2]


# --------------------------------------------------------------------------
# Containment


def test_subviews_become_children():
    objects = [
        _obj(0, "UIView", ("UISubviews", 10, {"$ref": 1})),
        _obj(1, "NSMutableArray",
             ("UINibEncoderEmptyKey", 10, {"$ref": 2}),
             ("UINibEncoderEmptyKey", 10, {"$ref": 3})),
        _obj(2, "UILabel"),
        _obj(3, "UIButton"),
    ]
    roots = nib_layout.build_tree(objects)
    parent = next(node for node in roots if node["index"] == 0)
    assert [child["class"] for child in parent["children"]] == ["UILabel", "UIButton"]


def test_the_flat_registries_parent_nothing():
    # UINibObjectsKey names every object in the file. Reading it as containment
    # files each view under the registry as well as under its real superview.
    objects = [
        _obj(0, "NSObject",
             ("UINibObjectsKey", 10, {"$ref": 1}),
             ("UINibTopLevelObjectsKey", 10, {"$ref": 1})),
        _obj(1, "NSArray",
             ("UINibEncoderEmptyKey", 10, {"$ref": 2}),
             ("UINibEncoderEmptyKey", 10, {"$ref": 3})),
        _obj(2, "UIView", ("UISubviews", 10, {"$ref": 4})),
        _obj(3, "UILabel"),
        _obj(4, "NSMutableArray", ("UINibEncoderEmptyKey", 10, {"$ref": 3})),
    ]
    roots = nib_layout.build_tree(objects)
    registry = next(node for node in roots if node["index"] == 1)
    assert registry["children"] == []
    view = next(node for node in roots if node["index"] == 2)
    assert [child["index"] for child in view["children"]] == [3]
    assert [node["index"] for node in roots] == [0, 1, 2, 4]


def test_no_containment_key_names_a_flat_registry():
    for key in nib_layout._REGISTRY_KEYS:
        assert key not in nib_layout._CONTAINMENT_KEYS


def test_a_view_keeps_one_parent():
    objects = [
        _obj(0, "UITableViewCell",
             ("UISubviews", 10, {"$ref": 1}),
             ("UIContentView", 10, {"$ref": 2})),
        _obj(1, "NSMutableArray", ("UINibEncoderEmptyKey", 10, {"$ref": 2})),
        _obj(2, "UITableViewCellContentView"),
    ]
    roots = nib_layout.build_tree(objects)
    cell = next(node for node in roots if node["index"] == 0)
    assert [child["index"] for child in cell["children"]] == [2]


def test_a_containment_cycle_does_not_recurse():
    objects = [
        _obj(0, "UIView", ("UIContentView", 10, {"$ref": 1})),
        _obj(1, "UIView", ("UIContentView", 10, {"$ref": 0})),
    ]
    roots = nib_layout.build_tree(objects)
    assert [node["index"] for node in roots] == [0]
    assert [child["index"] for child in roots[0]["children"]] == [1]
    assert roots[0]["children"][0]["children"] == []


# --------------------------------------------------------------------------
# The fields the spec names


def test_a_view_reports_the_spec_named_fields():
    objects = [
        _obj(0, "UILabel",
             ("UIBounds", 8, {"$data_hex": _BOUNDS_HEX}),
             ("UICenter", 8, {"$data_hex": _CENTER_HEX}),
             ("UIAutoresizingMask", 0, 18),
             ("UIBackgroundColor", 10, {"$ref": 1}),
             ("UIFont", 10, {"$ref": 2}),
             ("UIHidden", 5, False),
             ("UIOpaque", 4, True),
             ("UITag", 0, 7)),
        _obj(1, "UIColor",
             ("UIRed", 6, 0.5), ("UIGreen", 6, 0.25), ("UIBlue", 6, 0.125),
             ("UIAlpha", 6, 1.0)),
        _obj(2, "UIFont",
             ("UIFontName", 10, {"$ref": 3}), ("UIFontPointSize", 7, 15.0)),
        _obj(3, "NSString",
             ("NS.bytes", 8, {"$data_hex": "48656c7665746963612d426f6c64",
                              "$text": "Helvetica-Bold"})),
    ]
    node = nib_layout.build_tree(objects)[0]
    assert node["class"] == "UILabel"
    assert node["frame"] == {"x": 0.0, "y": 44.0, "width": 768.0, "height": 960.0}
    assert node["autoresizing_mask"] == 18
    assert node["background_color"] == "rgba(0.5, 0.25, 0.125, 1)"
    assert node["font"] == "Helvetica-Bold 15pt"
    assert node["hidden"] is False
    assert node["opaque"] is True
    assert node["tag"] == 7


def test_a_class_swapper_reports_the_runtime_class():
    objects = [
        _obj(0, "UIClassSwapper",
             ("UIClassName", 10, {"$ref": 1}),
             ("UIOriginalClassName", 10, {"$ref": 2})),
        _obj(1, "NSString", ("NS.bytes", 8, {"$data_hex": "43617463685669657700"[:-2],
                                             "$text": "CatchView"})),
        _obj(2, "NSString", ("NS.bytes", 8, {"$data_hex": "5549566965 77".replace(" ", ""),
                                             "$text": "UIView"})),
    ]
    node = nib_layout.build_tree(objects)[0]
    assert node["class"] == "CatchView"
    assert node["encoded_class"] == "UIClassSwapper"
    assert node["original_class"] == "UIView"


def test_the_file_owner_reports_outlets_and_target_action_pairs():
    objects = [
        _obj(0, "UIProxyObject", ("UIProxiedObjectIdentifier", 10, {"$ref": 1})),
        _obj(1, "NSString", ("NS.bytes", 8, {"$text": "IBFilesOwner",
                                             "$data_hex": "494246696c65734f776e6572"})),
        _obj(2, "UIRuntimeOutletConnection",
             ("UILabel", 10, {"$ref": 3}),
             ("UISource", 10, {"$ref": 0}),
             ("UIDestination", 10, {"$ref": 5})),
        _obj(3, "NSString", ("NS.bytes", 8, {"$text": "toolbar",
                                             "$data_hex": "746f6f6c626172"})),
        _obj(4, "UIRuntimeEventConnection",
             ("UILabel", 10, {"$ref": 6}),
             ("UISource", 10, {"$ref": 5}),
             ("UIDestination", 10, {"$ref": 0}),
             ("UIEventMask", 0, 64)),
        _obj(5, "UIButton"),
        _obj(6, "NSString", ("NS.bytes", 8, {"$text": "attachPhoto:",
                                             "$data_hex": "61747461636850686f746f3a"})),
    ]
    roots = nib_layout.build_tree(objects)
    owner = next(node for node in roots if node["index"] == 0)
    assert owner["proxied_object"] == "IBFilesOwner"
    assert owner["outlets"] == [{"name": "toolbar", "holder": 0, "target": 5}]
    assert owner["actions"] == [
        {"action": "attachPhoto:", "control": 5, "target": 0, "event_mask": 64},
    ]
    control = next(node for node in roots if node["index"] == 5)
    assert control["actions"] == owner["actions"]


def test_the_rendered_report_labels_every_spec_named_field():
    objects = [
        _obj(0, "UIView",
             ("UIBounds", 8, {"$data_hex": _BOUNDS_HEX}),
             ("UICenter", 8, {"$data_hex": _CENTER_HEX}),
             ("UIAutoresizingMask", 0, 18)),
    ]
    text = nib_layout.render_markdown("Sample", nib_layout.build_tree(objects))
    for label in ("class:", "frame:", "raw UIBounds:", "raw UICenter:",
                  "autoresizing mask:", "background color:", "hidden:",
                  "opaque:", "tag:", "raw values:"):
        assert label in text, label


# --------------------------------------------------------------------------
# The shipped bundle


def test_all_seventeen_nibs_render_without_raising(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        roots = nib_layout.build_tree(nibarchive.resolve(archive))
        text = nib_layout.render_markdown(path.stem, roots)
        assert text.startswith("# %s" % path.stem), path.name


def test_the_bundled_nibs_recover_real_geometry(nib_paths):
    def walk(node):
        yield node
        for child in node["children"]:
            yield from walk(child)

    # Every object keeps at most one parent, so a visit count equal to the
    # object count proves that the tree holds each object exactly once. The
    # counts below were measured against the 17 shipped NIB files.
    visits = 0
    declared = 0
    framed = set()
    off_origin = 0
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        objects = nibarchive.resolve(archive)
        declared += len(objects)
        for root in nib_layout.build_tree(objects):
            for node in walk(root):
                visits += 1
                if node["frame"] is None:
                    continue
                framed.add((path.name, node["index"]))
                if node["frame"]["x"] or node["frame"]["y"]:
                    off_origin += 1
    assert declared == 1143
    assert visits == declared
    assert len(framed) == 120
    # The string-matching reader recovered no frame at all, and a reader that
    # mistook UIBounds for the frame would place all 120 views at the origin.
    assert off_origin == 67


def test_every_geometry_bearing_object_reaches_the_report(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        objects = nibarchive.resolve(archive)
        expected = {
            obj["index"] for obj in objects
            if "UIBounds" in obj["properties_by_key"]
            and "UICenter" in obj["properties_by_key"]
        }
        text = nib_layout.render_markdown(
            path.stem, nib_layout.build_tree(objects))
        printed = text.count("- frame: (")
        assert printed == len(expected), path.name


def test_the_rendered_report_prints_a_recovered_frame_below_the_toolbar(nib_paths):
    by_name = {path.stem: path for path in nib_paths}
    path = by_name["PadNoteViewController"]
    archive = nibarchive.parse(path.read_bytes())
    roots = nib_layout.build_tree(nibarchive.resolve(archive))
    text = nib_layout.render_markdown(path.stem, roots)
    # Bounds (0, 0, 768, 960) with center (384, 524) is a view sitting below a
    # 44 point toolbar, so the frame origin is (0, 44) and not (0, 0).
    assert "frame: (0, 44, 768, 960)" in text
    assert "raw UIBounds: (0, 0, 768, 960)" in text
    assert "raw UICenter: (384, 524)" in text


def test_no_report_hangs_a_view_under_a_flat_registry(nib_paths):
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        objects = nibarchive.resolve(archive)
        by_index = {obj["index"]: obj for obj in objects}
        registry_arrays = {
            entry["value"]["$ref"]
            for obj in objects
            for entry in obj["properties"]
            if entry["key"] in nib_layout._REGISTRY_KEYS
            and isinstance(entry["value"], dict) and "$ref" in entry["value"]
        }
        assert registry_arrays, path.name
        roots = nib_layout.build_tree(objects)
        stack = list(roots)
        while stack:
            node = stack.pop()
            if node["index"] in registry_arrays:
                assert node["children"] == [], (path.name, node["index"])
            stack.extend(node["children"])
        # Every registry array is still present, and still lists its elements
        # among its raw values, so nothing the parser recovered is lost.
        seen = {node["index"] for node in roots}
        for index in registry_arrays:
            assert index in seen, (path.name, index)
            elements = [
                entry for entry in by_index[index]["properties"]
                if entry["key"] == nib_layout._ELEMENT_KEY
            ]
            reported = [
                entry for entry in next(n for n in roots if n["index"] == index)["raw"]
                if entry["key"] == nib_layout._ELEMENT_KEY
            ]
            assert reported == elements, (path.name, index)
def test_the_report_prints_every_object_exactly_once(nib_paths):
    import re

    header = re.compile(r"^ *- \*\*.+\*\* \(object (\d+)\)$")
    for path in nib_paths:
        archive = nibarchive.parse(path.read_bytes())
        objects = nibarchive.resolve(archive)
        text = nib_layout.render_markdown(
            path.stem, nib_layout.build_tree(objects))
        printed = [
            int(match.group(1))
            for match in (header.match(line) for line in text.splitlines())
            if match
        ]
        assert sorted(printed) == [obj["index"] for obj in objects], path.name
