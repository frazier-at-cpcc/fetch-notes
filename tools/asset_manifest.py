#!/usr/bin/env python3
"""Catalog the bundle's assets and generate an Xcode asset catalog.

The manifest is committed and the catalog is not. A reader compares digests and
confirms that a generated catalog matches the archived original, while the
repository never stores the images themselves.

**Asset identity** is the rule this module applies when it decides whether two
PNG files are two resolutions of one image or two separate images. The rule has
two clauses.

1. **Scale marker.** The marker is "@2x" or "@3x" and it may appear anywhere in
   the file stem, not only at the end. iOS writes the marker before the device
   suffix, so "Default-Landscape@2x~ipad.png" carries a scale of 2. Removing the
   marker yields the base name. A stem with no marker has a scale of 1.
2. **Device suffix.** The suffix "~ipad" or "~iphone" belongs to the asset
   identity, not to the scale. UIKit selects between a "~ipad" asset and a
   "~iphone" asset by device and then selects a resolution within the chosen
   asset. The suffix therefore stays in the base name, and
   "Default-Landscape~ipad" is one image set holding scales 1 and 2.

An earlier rule stripped only a trailing "@2x". Under that rule every one of the
28 device-suffixed files parsed as scale 1, so a retina image was recorded at
the size of its own standard-resolution sibling and would ship at half its
intended dimensions.

**Non-PNG resources** are collected from the whole bundle tree rather than from
the top level alone, because the localized .strings files live in per-language
*.lproj directories. Each one is keyed by its path relative to the bundle root,
so the localizations stay distinguishable from one another.
"""

import hashlib
import json
import os
import re
import shutil
import struct
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
OTHER_RESOURCE_SUFFIXES = (".ttf", ".css", ".js", ".strings")
SCALE_MARKER = re.compile(r"@([23])x")
DEVICE_SUFFIXES = ("~ipad", "~iphone")
SKIP_DIRS = ("_CodeSignature",)


def png_size(path):
    """Return (width, height) from the IHDR chunk without decoding pixels."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != PNG_SIGNATURE or head[12:16] != b"IHDR":
        raise ValueError("%s is not a PNG" % path)
    return struct.unpack(">II", head[16:24])


def split_scale(name):
    """Return (base_name, scale) under the asset-identity rule.

    The scale marker is located anywhere in the stem and removed. Any device
    suffix stays in the returned base name.
    """
    stem = name[:-4] if name.endswith(".png") else name
    match = None
    for match in SCALE_MARKER.finditer(stem):
        pass
    if match is None:
        return stem, 1
    base = stem[:match.start()] + stem[match.end():]
    return base, int(match.group(1))


def has_device_suffix(name):
    """Return True when the file stem ends in a device suffix."""
    stem = name[:-4] if name.endswith(".png") else name
    return stem.endswith(DEVICE_SUFFIXES)


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _walk(bundle):
    """Yield (relative_path, absolute_path) for every file in the bundle."""
    for root, dirs, files in os.walk(bundle):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            path = os.path.join(root, name)
            yield os.path.relpath(path, bundle), path


def build(bundle):
    """Walk the bundle and return the manifest document."""
    images = {}
    others = {}
    device_suffixed = 0
    for relative, path in _walk(bundle):
        name = os.path.basename(relative)
        if name.endswith(".png"):
            stem, scale = split_scale(name)
            prefix = os.path.dirname(relative)
            base = os.path.join(prefix, stem) if prefix else stem
            width, height = png_size(path)
            if has_device_suffix(name):
                device_suffixed += 1
            entry = images.setdefault(base, {"scales": {}})
            entry["scales"][str(scale)] = {
                "file": relative,
                "width": width,
                "height": height,
                "bytes": os.path.getsize(path),
                "sha256": _sha256(path),
            }
        elif name.endswith(OTHER_RESOURCE_SUFFIXES):
            others[relative] = {"bytes": os.path.getsize(path),
                                "sha256": _sha256(path)}

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
            "device_suffixed_png": device_suffixed,
            "other_resources": len(others),
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
        imageset = os.path.join(dest, "%s.imageset" % base.replace(os.sep, "_"))
        os.makedirs(imageset, exist_ok=True)
        entries = []
        for scale in sorted(entry["scales"]):
            relative = entry["scales"][scale]["file"]
            filename = os.path.basename(relative)
            shutil.copy2(os.path.join(bundle, relative),
                         os.path.join(imageset, filename))
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
          "%(paired)d paired, %(single_resolution)d single-resolution, "
          "%(device_suffixed_png)d device-suffixed PNG files, "
          "%(other_resources)d other resources" % manifest["counts"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
