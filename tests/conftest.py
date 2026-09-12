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
