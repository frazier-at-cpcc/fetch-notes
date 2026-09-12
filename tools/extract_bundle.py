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
