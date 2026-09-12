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
