# Catch Notes 5.2.8 Recovery

This repository holds the tooling and the research notes that reconstruct the asset
layer and the interface layout of Catch Notes 5.2.8, the final iOS build of a notes
application that shut down in 2013. The artifact is an armv7 IPA preserved by the
Internet Archive. The repository describes that artifact. It never stores it.

## What the repository holds

| Path | Contents |
|---|---|
| `tools/` | Four command line tools and one Objective-C metadata dumper, standard library only, plus four Ghidra scripts under `tools/ghidra/` |
| `tests/` | The pytest suite that pins every format fact the tools rely on |
| `research/` | The committed derived outputs: the teardown, the asset manifest, the layout reports, the NIB coverage gap, and the capture wheel geometry |
| `docs/superpowers/` | The P0 design spec and the implementation plan |
| `build/` | Everything unpacked from the IPA. Git ignores this directory in full. |

`tools/extract_bundle.py` verifies the pinned MD5 digest and unpacks the archive.
`tools/nibarchive.py` decodes the NIBArchive container format and knows nothing about
UIKit. `tools/nib_layout.py` interprets a decoded graph as view geometry and knows
nothing about file formats. `tools/asset_manifest.py` catalogs the images and generates
an Xcode asset catalog. The format layer and the interpretation layer stay separate, so
a disputed interpretation never requires editing verified parsing code.

## Quick start

```bash
pip install pytest
tools/run_p0.sh path/to/Catch.ipa
python3 -m pytest tests/ -v
```

The pipeline script regenerates every derived output under `research/` from a bare clone
plus the IPA. `tools/run_p0.sh --check path/to/Catch.ipa` runs the same pipeline into
`build/check/research`, diffs the result against the committed outputs, and exits
non-zero on any drift. That check passes on the current tree.

Tests that need the unpacked bundle skip when it is absent, so the suite stays green for
anyone who has not supplied their own copy of the artifact. With the bundle present, 64
tests pass. Without it, 36 tests pass and 28 skip.

The pinned artifact carries MD5 `9a891d439c74198cfa32e39a37e6bb34`. Every tool that
reads the IPA verifies that digest before it reads anything else. Two contributors who
run the pipeline either produce byte-identical output or learn immediately that their
artifacts differ.

## What the pipeline recovers

Every figure below comes from the tool that emits it, not from arithmetic over other
figures. The pipeline prints the asset counts and the metadata counts on each run, and
`research/nib-coverage.md` carries the NIB counts.

**Assets.** The bundle holds 546 PNG files across 277 image sets. 269 of those sets hold
more than one scale and 8 hold a single resolution. 28 PNG file names carry a device
suffix. The bundle holds 16 other resources, among them the font, the stylesheets, the
scripts, and the localized strings.

**Interface.** The bundle ships 17 NIB files. The layout reports recover 120 view
frames from them, and 67 of those frames sit at a non-zero origin. A frame is computed
rather than stored: `UIBounds` carries the size with an origin of 0, `UICenter` carries
the position, and the frame follows as origin = center - size / 2. Every report prints
both source values beside the computed frame.

**Metadata.** The Objective-C dumper reads 264 classes, 6938 methods, and 1706 instance
variables out of the armv7 executable.

**Coverage gap.** The binary declares 47 view controller classes. 17 NIB files cover 11
of them, so `research/nib-coverage.md` names the 36 classes that P3 must recover by
decompilation.

## No copyrighted bytes in git

Catch Notes remains under copyright. This repository commits descriptions of the
artifact and never the artifact itself. Images, fonts, stylesheets, scripts, localized
strings, the binary, and the IPA all land under `build/`, which `.gitignore` excludes.
The committed outputs are manifests, layout reports, and analysis prose. A reader who
wants to confirm a claim supplies the IPA and reruns the pipeline.

The asset manifest records a SHA-256 digest for every image rather than the image. A
reader compares digests and confirms that a generated asset catalog matches the archived
original, while the repository stores no pixel of it.

## Unresolved licensing question

The bundle ships `jr_hand.ttf`, a third-party handwriting typeface that the original
interface uses throughout. The redistribution terms for that font remain unknown. No
license file accompanies it in the bundle, and the analysis has not yet identified the
foundry or the license under which Catch shipped it. P3 must resolve those terms before
any rebuild ships the original typography. Two outcomes close the question. Either the
license permits redistribution, and the rebuild uses the original face, or it does not,
and the rebuild substitutes a metrically similar face and documents the substitution as
a deliberate deviation.

## Further reading

- `research/catch-notes-5.2.8-teardown.md` records the provenance of the artifact, the
  tools that work against a 2013 armv7 binary, and the results of the first static pass.
- `research/nib-layouts/` holds one Markdown report and one JSON graph per NIB file, 17
  of each.
- `research/piemenu-geometry.md` records the capture wheel geometry and the exact Ghidra
  procedure that recovered it.
- `docs/superpowers/specs/2026-09-12-p0-asset-layout-recovery-design.md` states the P0
  design and the constraints every tool honors.
- `research/nib-coverage.md` names the view controllers that ship no NIB and therefore
  require decompilation rather than extraction.
