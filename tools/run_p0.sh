#!/usr/bin/env bash
# tools/run_p0.sh: regenerate every P0 output from a verified IPA.
# Usage: tools/run_p0.sh [--check] <path-to-Catch.ipa>
#   --check  regenerate into build/check/research and diff against the
#            committed research outputs; exit 1 on any drift.
set -euo pipefail

CHECK=0
if [ "${1:-}" = "--check" ]; then
  CHECK=1
  shift
fi

IPA="${1:?usage: tools/run_p0.sh [--check] <path-to-Catch.ipa>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ "$CHECK" -eq 1 ]; then
  OUT="build/check/research"
  WORK="build/check"
  rm -rf "$OUT"
else
  OUT="research"
  WORK="build"
fi
mkdir -p "$OUT"

python3 -m tools.extract_bundle "$IPA" build
APP="build/Payload/Catch.app"

mkdir -p "$OUT/nib-layouts"
for nib in "$APP"/*.nib "$APP"/*.lproj/*.nib; do
  [ -e "$nib" ] || continue
  name="$(basename "$nib" .nib)"
  python3 -m tools.nibarchive "$nib" -o "$OUT/nib-layouts/${name}.json"
  python3 -m tools.nib_layout "$nib" -o "$OUT/nib-layouts/${name}.md"
done

python3 -m tools.asset_manifest "$APP" \
  -m "$OUT/asset-manifest.json" \
  -x "$WORK/Catch.xcassets"

python3 tools/objc_dump32.py "$APP/Catch" --headers "$WORK/headers"

# NIB coverage: every view controller class in the dumped headers that no NIB
# file names. A NIB stem loses a trailing _iPad or _iPhone before the match.
APP="$APP" HEADERS="$WORK/headers" OUT="$OUT" python3 - <<'PY'
import glob
import os
import re

app = os.environ["APP"]
headers = os.environ["HEADERS"]
out = os.environ["OUT"]

classes = sorted(
    os.path.basename(p)[:-2] for p in glob.glob(os.path.join(headers, "*ViewController.h"))
)
nibs = sorted(
    glob.glob(os.path.join(app, "*.nib")) + glob.glob(os.path.join(app, "*.lproj", "*.nib"))
)
covered = {re.sub(r"_(iPad|iPhone)$", "", os.path.basename(p)[:-4]) for p in nibs}
missing = [c for c in classes if c not in covered]

lines = [
    "# NIB Coverage",
    "",
    f"The bundle ships {len(nibs)} NIB files for {len(classes)} view controller classes.",
    f"P3 recovers the following {len(missing)} layouts by decompilation, because no NIB",
    "describes them.",
    "",
]
lines += [f"- `{c}`" for c in missing]
with open(os.path.join(out, "nib-coverage.md"), "w") as fh:
    fh.write("\n".join(lines) + "\n")
PY

if [ "$CHECK" -eq 1 ]; then
  status=0
  diff -ru research/nib-layouts "$OUT/nib-layouts" || status=1
  diff -u research/asset-manifest.json "$OUT/asset-manifest.json" || status=1
  diff -u research/nib-coverage.md "$OUT/nib-coverage.md" || status=1
  if [ "$status" -ne 0 ]; then
    echo "DRIFT: committed research outputs differ from a fresh run." >&2
    exit 1
  fi
  echo "Check passed. Committed research outputs match a fresh run."
  exit 0
fi

echo "P0 complete. Committed outputs are under research/. Everything under build/ stays local."
