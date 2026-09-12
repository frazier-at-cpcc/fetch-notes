#!/usr/bin/env python3
"""Interpret a decoded NIB object graph as view geometry.

Interpretation carries risk, because value semantics differ between UIKit
classes. Every node therefore carries its untouched properties under "raw", in
file order, so a reader who disagrees with an interpretation inspects the
underlying value without rerunning the parser.

Two readings are load bearing and both were measured against the 17 NIB files
in Catch Notes 5.2.8 rather than assumed.

**Geometry.** The archive never stores a CGRect as text. It stores two type-8
payloads. `UIBounds` is 17 bytes: one tag byte 6 followed by four packed
little-endian float32 values that read as x, y, width and height. Its x and y
are 0 in all 120 occurrences, so `UIBounds` carries a size and not a position.
`UICenter` is 9 bytes: the same tag byte followed by two float32 values that
read as the center point. The position lives there. The frame therefore follows
from both values together, as origin = center - size / 2 and size = the size
`UIBounds` carries. Every node reports the raw bounds and the raw center beside
the computed frame, so the computation stays auditable.

**Containment.** A NIB holds several flat registries, among them
`UINibObjectsKey` and `UINibTopLevelObjectsKey`, each an array naming every
archived object. Reading those arrays as parents asserts a second hierarchy
that the interface never had, and it files a view under a registry as well as
under its real superview. Only the keys in `_CONTAINMENT_KEYS` establish a
parent, and every object keeps exactly one parent.
"""

import sys

from tools import nibarchive

# Keys through which one view contains another. `UISubviews` names a mutable
# array of subviews; the other three keys name a single contained view each.
# Across the 17 NIB files, `UISubviews` establishes 88 parent-child edges and
# `UINavigationBar` establishes 4. `UIContentView` and `UITableHeaderView`
# establish none, because each names a view that `UISubviews` already parents,
# and a view keeps the first parent that claims it.
_CONTAINMENT_KEYS = (
    "UISubviews",
    "UIContentView",
    "UITableHeaderView",
    "UINavigationBar",
)

# Flat registries. Each names an array of every object of some kind in the
# file, so none of them describes containment. They are listed to record the
# exclusion; membership of `_CONTAINMENT_KEYS` is what actually grants
# parenthood.
_REGISTRY_KEYS = (
    "UINibObjectsKey",
    "UINibTopLevelObjectsKey",
    "UINibConnectionsKey",
    "UINibVisibleWindowsKey",
    "UINibAccessibilityConfigurationsKey",
    "UINibKeyValuePairsKey",
)

_ARRAY_CLASSES = ("NSArray", "NSMutableArray")

# The key an array uses for each of its elements. It repeats once per element,
# which is why an object's properties arrive as an ordered list.
_ELEMENT_KEY = "UINibEncoderEmptyKey"

_OUTLET_CLASS = "UIRuntimeOutletConnection"
_EVENT_CLASS = "UIRuntimeEventConnection"


# --------------------------------------------------------------------------
# Reading one resolved object


def entries(obj):
    """Return an object's value entries as a list in file order.

    tools/nibarchive.py emits `properties` as that list. An object assembled by
    hand may carry only `properties_by_key`, so that mapping is flattened when
    the list is absent.
    """
    values = obj.get("properties")
    if values is not None:
        return list(values)
    flattened = []
    for group in obj.get("properties_by_key", {}).values():
        flattened.extend(group)
    return flattened


def _by_key(obj):
    """Return the key -> entries mapping, deriving it when it is absent."""
    indexed = obj.get("properties_by_key")
    if indexed is not None:
        return indexed
    derived = {}
    for entry in entries(obj):
        derived.setdefault(entry["key"], []).append(entry)
    return derived


def first(obj, key):
    """Return the value of the first entry carrying `key`, or None."""
    group = _by_key(obj).get(key)
    if not group:
        return None
    return group[0].get("value")


def _ref(value):
    """Return the object index a reference value names, or None."""
    if isinstance(value, dict) and "$ref" in value:
        return value["$ref"]
    return None


# --------------------------------------------------------------------------
# Geometry


def parse_bounds(value):
    """Return the size `UIBounds` carries, or None when the value is not one.

    The payload holds four float32 values. The first two are the origin of the
    bounds rectangle, which is 0 in every occurrence in the bundle, so they are
    reported unaltered rather than folded into the frame.
    """
    floats = nibarchive.decode_packed_floats(value)
    if floats is None or len(floats) != 4:
        return None
    x, y, width, height = floats
    return {"x": x, "y": y, "width": width, "height": height}


def parse_center(value):
    """Return the point `UICenter` carries, or None when the value is not one."""
    floats = nibarchive.decode_packed_floats(value)
    if floats is None or len(floats) != 2:
        return None
    return {"x": floats[0], "y": floats[1]}


def compute_frame(bounds, center):
    """Return the frame a bounds size and a center point describe, or None.

    The size comes from the bounds. The origin is the center less half the
    size, which is the definition UIKit uses to place a view in its superview.
    """
    if bounds is None or center is None:
        return None
    return {
        "x": center["x"] - bounds["width"] / 2.0,
        "y": center["y"] - bounds["height"] / 2.0,
        "width": bounds["width"],
        "height": bounds["height"],
    }


def view_geometry(obj):
    """Return {"frame", "bounds", "center"} for one object, or None."""
    bounds = parse_bounds(first(obj, "UIBounds"))
    center = parse_center(first(obj, "UICenter"))
    if bounds is None and center is None:
        return None
    return {"frame": compute_frame(bounds, center), "bounds": bounds, "center": center}


# --------------------------------------------------------------------------
# Named values the spec asks each view to report


def _string_of(objects_by_index, index):
    """Return the text an NSString object holds, or None."""
    obj = objects_by_index.get(index)
    if obj is None:
        return None
    value = first(obj, "NS.bytes")
    if isinstance(value, dict):
        text = value.get("$text")
        if isinstance(text, str):
            return text
    if isinstance(value, str):
        return value
    return None


def describe_color(objects_by_index, index):
    """Describe a UIColor object as a short string, or return None."""
    obj = objects_by_index.get(index)
    if obj is None:
        return None
    name_ref = _ref(first(obj, "UISystemColorName"))
    if name_ref is not None:
        name = _string_of(objects_by_index, name_ref)
        if name:
            return "system color %s" % name
    alpha = first(obj, "UIAlpha")
    white = first(obj, "UIWhite")
    if white is not None:
        return "white %g alpha %g" % (white, alpha if alpha is not None else 1.0)
    red = first(obj, "UIRed")
    green = first(obj, "UIGreen")
    blue = first(obj, "UIBlue")
    if None not in (red, green, blue):
        return "rgba(%g, %g, %g, %g)" % (
            red, green, blue, alpha if alpha is not None else 1.0
        )
    return "object %d" % index


def describe_font(objects_by_index, index):
    """Describe a UIFont object as a short string, or return None."""
    obj = objects_by_index.get(index)
    if obj is None:
        return None
    size = first(obj, "UIFontPointSize")
    if size is None:
        size = first(obj, "NSSize")
    name_ref = _ref(first(obj, "UIFontName"))
    if name_ref is None:
        name_ref = _ref(first(obj, "NSName"))
    name = _string_of(objects_by_index, name_ref) if name_ref is not None else None
    if name is None:
        name = "system font" if first(obj, "UISystemFont") else "object %d" % index
    if size is None:
        return name
    return "%s %gpt" % (name, size)


def _class_label(objects_by_index, obj):
    """Return the class a node reports.

    Interface Builder encodes a view whose runtime class is a subclass as a
    UIClassSwapper carrying both names. The node reports the runtime class and
    keeps the encoded one beside it.
    """
    encoded = obj["class"]
    if encoded != "UIClassSwapper":
        return encoded, None
    runtime_ref = _ref(first(obj, "UIClassName"))
    original_ref = _ref(first(obj, "UIOriginalClassName"))
    runtime = _string_of(objects_by_index, runtime_ref) if runtime_ref is not None else None
    original = (
        _string_of(objects_by_index, original_ref) if original_ref is not None else None
    )
    if runtime is None:
        return encoded, None
    return runtime, original


def _connections(objects, objects_by_index):
    """Return outlet and action records keyed by the object index they belong to.

    An outlet belongs to the object that holds it, which the archive names as
    the connection source. An action pairs a control with a target, and the
    record is filed under both ends so that either node reports the pair. Each
    record names both ends, so the pair reads the same from either side.
    """
    outlets = {}
    actions = {}
    for obj in objects:
        kind = obj["class"]
        if kind not in (_OUTLET_CLASS, _EVENT_CLASS):
            continue
        label_ref = _ref(first(obj, "UILabel"))
        label = _string_of(objects_by_index, label_ref) if label_ref is not None else None
        source = _ref(first(obj, "UISource"))
        destination = _ref(first(obj, "UIDestination"))
        if kind == _OUTLET_CLASS:
            record = {"name": label, "holder": source, "target": destination}
            outlets.setdefault(source, []).append(record)
        else:
            record = {
                "action": label,
                "control": source,
                "target": destination,
                "event_mask": first(obj, "UIEventMask"),
            }
            actions.setdefault(source, []).append(record)
            if destination != source:
                actions.setdefault(destination, []).append(record)
    return outlets, actions


# --------------------------------------------------------------------------
# Tree assembly


def _contained_refs(obj, objects_by_index):
    """Yield (child index, key) for every view this object contains.

    A containment key names either the contained view or an array of contained
    views. Nothing else parents anything, so the flat registries named in
    `_REGISTRY_KEYS` contribute no edges.
    """
    for entry in entries(obj):
        key = entry["key"]
        if key not in _CONTAINMENT_KEYS:
            continue
        index = _ref(entry.get("value"))
        if index is None:
            continue
        target = objects_by_index.get(index)
        if target is None:
            continue
        if target["class"] in _ARRAY_CLASSES:
            for element in entries(target):
                if element["key"] != _ELEMENT_KEY:
                    continue
                child = _ref(element.get("value"))
                if child is not None:
                    yield child, key
        else:
            yield index, key


def build_tree(objects):
    """Assemble root nodes, parenting each object through view containment only.

    Every object becomes a node, so nothing the parser recovered disappears
    from the report. An object receives at most one parent: the first
    containment reference to it in object order wins, and a reference that
    would close a cycle is refused. Objects that no view contains come back as
    roots, in index order.
    """
    objects_by_index = {obj["index"]: obj for obj in objects}
    outlets, actions = _connections(objects, objects_by_index)

    nodes = {}
    for obj in objects:
        index = obj["index"]
        class_name, original_class = _class_label(objects_by_index, obj)
        geometry = view_geometry(obj)
        background_ref = _ref(first(obj, "UIBackgroundColor"))
        font_ref = _ref(first(obj, "UIFont"))
        nodes[index] = {
            "index": index,
            "class": class_name,
            "encoded_class": obj["class"],
            "original_class": original_class,
            "frame": geometry["frame"] if geometry else None,
            "bounds": geometry["bounds"] if geometry else None,
            "center": geometry["center"] if geometry else None,
            "autoresizing_mask": first(obj, "UIAutoresizingMask"),
            "background_color": (
                describe_color(objects_by_index, background_ref)
                if background_ref is not None else None
            ),
            "font": (
                describe_font(objects_by_index, font_ref)
                if font_ref is not None else None
            ),
            "hidden": first(obj, "UIHidden"),
            "opaque": first(obj, "UIOpaque"),
            "tag": first(obj, "UITag"),
            "proxied_object": (
                _string_of(objects_by_index, _ref(first(obj, "UIProxiedObjectIdentifier")))
                if _ref(first(obj, "UIProxiedObjectIdentifier")) is not None else None
            ),
            "outlets": outlets.get(index, []),
            "actions": actions.get(index, []),
            "raw": entries(obj),
            "children": [],
        }

    parent_of = {}

    def _would_cycle(parent, child):
        seen = parent
        while seen is not None:
            if seen == child:
                return True
            seen = parent_of.get(seen)
        return False

    for obj in objects:
        index = obj["index"]
        for child, _key in _contained_refs(obj, objects_by_index):
            if child == index or child in parent_of or child not in nodes:
                continue
            if _would_cycle(index, child):
                continue
            parent_of[child] = index
            nodes[index]["children"].append(nodes[child])

    return [node for index, node in sorted(nodes.items()) if index not in parent_of]


# --------------------------------------------------------------------------
# Rendering


def _rect(rect):
    return "(%g, %g, %g, %g)" % (rect["x"], rect["y"], rect["width"], rect["height"])


def _point(point):
    return "(%g, %g)" % (point["x"], point["y"])


def _flag(value):
    if value is None:
        return "not encoded"
    return "true" if value else "false"


def _object_label(nodes_by_index, index):
    node = nodes_by_index.get(index)
    if node is None:
        return "object %s" % index
    return "object %d (%s)" % (index, node["class"])


# The per-view node fields the spec names beyond the geometry. A node that
# carries any of them reports all of them, so a reader comparing two views
# finds the same labels in the same order and reads "not encoded" where the
# archive supplied nothing.
_VIEW_FIELDS = ("bounds", "center", "autoresizing_mask", "background_color",
                "font", "hidden", "opaque", "tag")


def _field_lines(node, nodes_by_index, indent):
    """Return the labelled per-view fields the spec names, in a fixed order."""
    lines = []
    is_view = any(node[field] is not None for field in _VIEW_FIELDS)

    def add(label, text):
        lines.append("%s  - %s: %s" % (indent, label, text))

    add("class", "`%s`" % node["class"])
    if node["original_class"]:
        add("encoded as", "`%s` swapping `%s`"
            % (node["encoded_class"], node["original_class"]))
    if node["frame"] is not None:
        add("frame", _rect(node["frame"]))
    if node["bounds"] is not None:
        add("raw UIBounds", _rect(node["bounds"]))
    if node["center"] is not None:
        add("raw UICenter", _point(node["center"]))
    if is_view:
        add("autoresizing mask",
            "not encoded" if node["autoresizing_mask"] is None
            else str(node["autoresizing_mask"]))
        add("background color", node["background_color"] or "not encoded")
        if node["font"]:
            add("font", node["font"])
        add("hidden", _flag(node["hidden"]))
        add("opaque", _flag(node["opaque"]))
        add("tag", "not encoded" if node["tag"] is None else str(node["tag"]))
    for outlet in node["outlets"]:
        add("outlet", "`%s` to %s"
            % (outlet["name"], _object_label(nodes_by_index, outlet["target"])))
    for action in node["actions"]:
        mask = action["event_mask"]
        add("target/action", "`%s` from %s to %s, event mask %s" % (
            action["action"],
            _object_label(nodes_by_index, action["control"]),
            _object_label(nodes_by_index, action["target"]),
            "not encoded" if mask is None else mask,
        ))
    return lines


def _render_node(node, depth, lines, nodes_by_index):
    indent = "  " * depth
    lines.append("%s- **%s** (object %d)" % (indent, node["class"], node["index"]))
    lines.extend(_field_lines(node, nodes_by_index, indent))
    lines.append("%s  - raw values:" % indent)
    for entry in node["raw"]:
        lines.append("%s    - `%s` (type %d): `%r`"
                     % (indent, entry["key"], entry["type"], entry.get("value")))
    for child in node["children"]:
        _render_node(child, depth + 1, lines, nodes_by_index)


def _index_nodes(roots):
    nodes_by_index = {}
    stack = list(roots)
    while stack:
        node = stack.pop()
        nodes_by_index[node["index"]] = node
        stack.extend(node["children"])
    return nodes_by_index


def _carries_interface(node):
    """Report whether a subtree holds geometry, containment, or a connection."""
    stack = [node]
    while stack:
        current = stack.pop()
        if (current["frame"] is not None or current["children"]
                or current["outlets"] or current["actions"]):
            return True
        stack.extend(current["children"])
    return False


def render_markdown(name, roots):
    """Produce the committed layout report for one NIB.

    The report opens with the interface: every root that holds geometry, a
    contained view, or a connection, rendered with its subtree. The remaining
    roots follow under their own heading. Both sections carry the same detail,
    so the split orders the report without removing anything from it.
    """
    nodes_by_index = _index_nodes(roots)
    interface = [root for root in roots if _carries_interface(root)]
    supporting = [root for root in roots if not _carries_interface(root)]
    lines = [
        "# %s" % name,
        "",
        "Recovered layout for `%s.nib`. Every interpreted value appears beside the" % name,
        "raw decoded value, so a disputed reading stays auditable.",
        "",
        "The frame is computed, not stored. `UIBounds` carries the size and an",
        "origin that is always 0, and `UICenter` carries the position, so the frame",
        "is origin = center - size / 2 with the size taken from the bounds. Both",
        "source values appear beside every frame.",
        "",
        "A view is nested under another view only through a containment key: %s."
        % ", ".join("`%s`" % key for key in _CONTAINMENT_KEYS),
        "The flat registries, among them `UINibObjectsKey` and",
        "`UINibTopLevelObjectsKey`, name every archived object and describe no",
        "containment, so they parent nothing.",
        "",
        "## Interface",
        "",
    ]
    for root in interface:
        _render_node(root, 0, lines, nodes_by_index)
        lines.append("")
    lines += [
        "## Supporting objects",
        "",
        "These objects carry no geometry, contain no view, and hold no",
        "connection. They remain here because a reader auditing an",
        "interpretation follows a reference into them.",
        "",
    ]
    for root in supporting:
        _render_node(root, 0, lines, nodes_by_index)
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
