import json
import struct

from tools import asset_manifest


def _png(tmp_path, name, width, height):
    ihdr = struct.pack(">II", width, height) + b"\x08\x06\x00\x00\x00"
    data = (b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + ihdr
            + b"\x00\x00\x00\x00")
    path = tmp_path / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def test_png_size_reads_ihdr(tmp_path):
    assert asset_manifest.png_size(_png(tmp_path, "a.png", 320, 44)) == (320, 44)


def test_split_scale_separates_retina_suffix():
    assert asset_manifest.split_scale("icon@2x.png") == ("icon", 2)
    assert asset_manifest.split_scale("icon@3x.png") == ("icon", 3)
    assert asset_manifest.split_scale("icon.png") == ("icon", 1)


def test_split_scale_reads_marker_before_device_suffix():
    """The scale marker sits before the device suffix, and the suffix is identity."""
    assert asset_manifest.split_scale("Default-Landscape@2x~ipad.png") == (
        "Default-Landscape~ipad", 2)
    assert asset_manifest.split_scale("Default-Landscape~ipad.png") == (
        "Default-Landscape~ipad", 1)
    assert asset_manifest.split_scale("Tag@2x~iphone.png") == ("Tag~iphone", 2)


def test_device_suffixed_variants_pair(tmp_path):
    _png(tmp_path, "Splash~ipad.png", 34, 45)
    _png(tmp_path, "Splash@2x~ipad.png", 68, 90)
    _png(tmp_path, "Splash~iphone.png", 20, 30)
    manifest = asset_manifest.build(str(tmp_path))
    assert manifest["counts"]["image_sets"] == 2
    assert manifest["counts"]["paired"] == 1
    assert manifest["counts"]["device_suffixed_png"] == 3
    pad = manifest["images"]["Splash~ipad"]
    assert pad["scales"]["1"]["width"] == 34
    assert pad["scales"]["2"]["width"] == 68


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


def test_other_resources_include_subdirectories(tmp_path):
    (tmp_path / "fr.lproj").mkdir()
    (tmp_path / "fr.lproj" / "Localizable.strings").write_text("a")
    (tmp_path / "de.lproj").mkdir()
    (tmp_path / "de.lproj" / "Localizable.strings").write_text("bb")
    (tmp_path / "app.js").write_text("ccc")
    manifest = asset_manifest.build(str(tmp_path))
    keys = sorted(manifest["other_resources"])
    assert keys == ["app.js", "de.lproj/Localizable.strings",
                    "fr.lproj/Localizable.strings"]
    assert manifest["other_resources"]["de.lproj/Localizable.strings"]["bytes"] == 2


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


def test_real_bundle_records_seven_strings_files(bundle_dir):
    """The bundle holds seven .strings files across six *.lproj directories.

    An earlier build() scanned only the bundle top level and recorded none of
    them. Each key carries its lproj directory, so the six localizations stay
    distinguishable and en.lproj contributes two files.
    """
    manifest = asset_manifest.build(str(bundle_dir))
    strings = sorted(key for key in manifest["other_resources"]
                     if key.endswith(".strings"))
    assert len(strings) == 7
    assert strings == [
        "de.lproj/Localizable.strings",
        "en.lproj/InfoPlist.strings",
        "en.lproj/Localizable.strings",
        "es.lproj/Localizable.strings",
        "fr.lproj/Localizable.strings",
        "ja.lproj/Localizable.strings",
        "ko.lproj/Localizable.strings",
    ]
    assert len({key.split("/")[0] for key in strings}) == 6


def test_real_bundle_matches_measured_counts(bundle_dir):
    """Counts measured from the staged bundle by running the tool.

    Command:
        build/venv/bin/python -m tools.asset_manifest build/Payload/Catch.app

    These assertions changed because the asset-identity rule changed. The earlier
    split_scale stripped only a trailing "@2x", so each of the 28 device-suffixed
    files parsed as scale 1 and formed its own set. That produced 291 image sets,
    255 paired and 36 single-resolution. Reading the scale marker before the
    device suffix pairs 14 of those files with their siblings, which removes 14
    sets, adds 14 paired sets and leaves 8 single-resolution sets.

    The 8 remaining single-resolution sets are genuine orphans in the artifact:
    four @2x files with no 1x sibling (Default-568h@2x, bg_overlay-568h@2x,
    text_overlay-568h@2x, btn_cap_checklist@2x) and four 1x files with no @2x
    sibling (NoteViewInputAccessory_KeyboardFadeLeft,
    NoteViewInputAccessory_KeyboardFadeRight, ReminderIcon, btn_cap_checklsit).
    The last pair of names differs by a transposition in the shipped file name.
    """
    manifest = asset_manifest.build(str(bundle_dir))
    assert manifest["counts"]["png_total"] == 546
    assert manifest["counts"]["image_sets"] == 277
    assert manifest["counts"]["paired"] == 269
    assert manifest["counts"]["single_resolution"] == 8
    assert manifest["counts"]["device_suffixed_png"] == 28
