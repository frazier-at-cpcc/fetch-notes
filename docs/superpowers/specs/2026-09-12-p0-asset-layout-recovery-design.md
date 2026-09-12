# P0: Asset and Layout Recovery

Design specification, 2026-09-12.

## Context

The `fetch-notes` project recreates Catch Notes 5.2.8 as a native 64-bit
application backed by CloudKit. The project classification is preservation. The
fidelity target covers look, feel, and interaction together, and the project
treats any deviation from the 2013 original as a documented defect rather than a
design choice.

That target creates a dependency. Every later claim of visual fidelity rests on
possessing the original artwork and the original layout geometry. P0 produces
both, and it produces the tooling that regenerates both from a verified copy of
the archived binary.

The teardown that precedes this work lives in
`research/catch-notes-5.2.8-teardown.md`. It establishes provenance for the
artifact and recovers the class list that P0 depends on.

## Scope

P0 delivers four tools and one manual analysis document.

P0 does not build any application target, define any domain model, or touch
CloudKit. Those belong to P1, P2, and P3.

### Goals

1. Regenerate the complete asset set from a hash-verified IPA on any machine.
2. Decode all 17 NIBArchive files into a readable object graph.
3. Express that object graph as layout reports carrying frames, autoresizing
   masks, colors, fonts, outlets, and actions.
4. Recover the capture wheel geometry from compiled code.
5. Keep every copyrighted byte out of a public repository.

### Non-goals

P0 does not recreate any asset by hand. P0 does not evaluate whether the
recovered layout is reproducible in SwiftUI or UIKit, because that evaluation
belongs to P3. P0 does not resolve font licensing, though it records the question.

## Constraints

The repository is public. The artwork, the font, the editor stylesheets, the
editor scripts, and the localized strings all remain under copyright. The
pipeline therefore separates two classes of output. Derived descriptions get
committed. Copyrighted bytes stay in a gitignored working directory.

A contributor reproduces the local half by supplying their own copy of the IPA.
The Internet Archive item `CatchiPA` distributes that copy.

## Established facts

The following facts come from direct measurement during design and they remove
several assumptions from the implementation.

| Fact | Consequence |
|---|---|
| Zero of the 546 PNG files use Apple CgBI optimization | The pipeline needs no `pngdefry` or `pngcrush` revert stage |
| The bundle holds 546 PNG files across 277 image sets: 269 paired, 8 single-resolution, 28 carrying a device suffix | The manifest models pairing rather than assuming it |
| **Asset identity** groups by stem with the scale marker removed from anywhere in the name, and treats a `~ipad` or `~iphone` suffix as part of identity rather than part of scale | Without this rule the same bundle yields three different counts |
| `UIBounds` is a `0x06`-prefixed float32 quad holding `(0, 0, width, height)`, so it carries size only. `UICenter` is a `0x06`-prefixed float32 pair holding the position. 120 views across the 17 NIBs carry both | The frame is computed as `origin = center - size / 2`, never read directly |
| All NIB files carry the 10-byte magic `NIBArchive` | `plutil` cannot read them, and a parser is required |
| `xcrun ibtool --convert` and `--dump` both fail with `Unable to rename classes, class name parsing failed` | Xcode tooling offers no path, and the parser is the only option |
| `PieMenu` draws through `CAShapeLayer` and bezier paths | The capture wheel requires decompilation, not asset extraction |

## Components

### 1. `tools/extract_bundle.py`

Accepts a path to the IPA. Computes the MD5 digest and compares it against the
pinned value `9a891d439c74198cfa32e39a37e6bb34`. Halts with a non-zero exit
status on any mismatch, because a differing artifact invalidates every downstream
measurement. Unpacks the verified archive into `build/Catch.app`.

The pinned hash makes the pipeline deterministic across machines. Two
contributors who both run the pipeline produce byte-identical output or the tool
tells them why they did not.

### 2. `tools/nibarchive.py`

Parses the NIBArchive container into a Python object graph and serializes that
graph as JSON.

The container opens with the 10-byte magic, which measurement confirms. The
header that follows declares version fields and four table descriptors covering
objects, keys, values, and class names, where each descriptor supplies a count
and a file offset. Objects reference a class name and a contiguous run of values.
Values pair a key index with a typed payload, and the type set covers signed
integers of several widths, single and double precision floats, the two boolean
constants, strings, raw data, nil, and object references. Integer fields use a
variable-length encoding terminated by a high bit.

Measurement during planning confirmed this description against all 17 files. The
four tables decode with every table ending at exactly the offset the header
declares for the next one, and the final table ending at the file size. All 17
files report format version 1.9. The parser still validates its own reading at
run time, because that check costs nothing and it catches a malformed input
before the layout stage misinterprets it.

The module exposes one entry point:

```python
def parse(path: str) -> dict:
    """Return {"classes": [...], "objects": [...], "keys": [...], "values": [...]}."""
```

The command line interface writes JSON to stdout or to a named file.

### 3. `tools/nib_layout.py`

Consumes the JSON graph and emits a layout report for one NIB.

The tool walks the object graph, identifies objects whose class name descends
from `UIView`, and reconstructs the parent and child relationships. For each view
it reports the class, the frame rectangle, the autoresizing mask, the background
color, the font when the view carries one, the hidden and opaque flags, and the
tag. For the file owner it reports outlet names and target and action pairs.

Interpretation carries risk, because value semantics differ between UIKit
classes. The tool therefore prints the raw decoded value next to every
interpretation it makes. A reader who disagrees with an interpretation can see
the underlying bytes without rerunning the parser.

Each report lands at `research/nib-layouts/<NibName>.md`, accompanied by
`<NibName>.json` holding the unabridged graph.

### 4. `tools/asset_manifest.py`

Walks the extracted bundle and produces two outputs from one pass.

The first output is `research/asset-manifest.json`, which the project commits. It
records for every PNG the base name, the resolution variant, the pixel width and
height, the byte size, and the SHA-256 digest. It groups single-resolution assets
separately from paired assets, because 28 assets ship at one resolution only. It
records the same identifying fields for `jr_hand.ttf`, for the four stylesheets,
for the four scripts, and for the seven `.strings` files.

The second output is an asset catalog written to `build/Catch.xcassets`, which
the project does not commit. The catalog carries correct `Contents.json` scale
declarations so that an application target consumes it without further work.

The manifest makes the catalog auditable. A reader compares digests and confirms
that a generated catalog matches the archived original without the repository
ever holding the images.

### 5. `research/piemenu-geometry.md`

A written analysis rather than a tool.

The capture wheel is the interaction that distinguishes Catch from every
contemporary note application, and it is the component P0 cannot extract. The
class dump shows that `PieMenu` composes `CAShapeLayer` instances for slices, a
`CAShapeLayer` content mask, an outer circle, a `UIImageView` inner circle, and a
`CircleView` inner circle lip. Three methods carry the geometry:

```objc
+ pathForSliceSegment:withCenterPoint:radius:;
- layoutIconViewsWithRadius:iconScale:;
+ pathAnimationWithDuration:timingFunctionName:fromPath:toPath:;
```

The analysis decompiles these three methods in Ghidra and reduces them to
concrete values: the slice count, the start angle, the sweep per slice, the inner
and outer radii, the icon placement radius and scale, the animation duration, and
the named timing function. The document states each recovered value and marks
separately any value it estimates rather than reads.

`_sprungOpen` and `_osSupportsInteractionDuringAnimation` appear as instance
variables, so the analysis also records the spring behavior and the interaction
rule that accompanies it.

## Verification

The parser admits an internal correctness check that needs no external oracle.
The header declares a count for each of the four tables. A correct parse yields
exactly those counts. The test suite asserts that equality for all 17 NIB files,
and a parse that produces a different count fails.

Three further checks complete the strategy.

1. **Coverage.** All 17 NIB files parse without raising.
2. **Golden fixture.** One parsed graph, chosen for structural variety, gets
   committed as a test fixture. The fixture stores structure and decoded values,
   and it stores no asset bytes. A later parser change that alters the fixture
   fails the suite.
3. **Reproducibility.** Running extraction twice produces identical SHA-256
   digests for every manifest entry.

The layout reports and the PieMenu analysis resist automated verification,
because both interpret rather than compute. Both therefore carry the raw values
beside the interpretation, which lets a human audit them.

## Repository layout

```
tools/
  objc_dump32.py          # exists
  extract_bundle.py       # new
  nibarchive.py           # new
  nib_layout.py           # new
  asset_manifest.py       # new
tests/
  test_nibarchive.py      # new
  fixtures/               # new, structure only
research/
  catch-notes-5.2.8-teardown.md   # exists
  asset-manifest.json             # new, committed
  piemenu-geometry.md             # new, committed
  nib-layouts/*.md, *.json        # new, committed
docs/superpowers/specs/
  2026-09-12-p0-asset-layout-recovery-design.md
build/                    # gitignored in full
```

The `.gitignore` already excludes `*.ipa`, `ipa/`, `Payload/`, `dump_headers/`,
and `headers_out/`. P0 adds `build/`.

## Risks

**The PieMenu constants may resist clean recovery.** Compiler optimization can
fold the geometry into instruction sequences that do not map back to named
values. The analysis then reports a range or an estimate. The mitigation is
disclosure rather than prevention, and the document labels every estimated value.

**Value semantics vary across UIKit classes.** The parser decodes types
correctly while the layout tool may misread meaning. Printing raw values beside
interpretations contains the damage, because a wrong interpretation stays
visible and correctable.

**The font carries unknown licensing.** `jr_hand.ttf` is third-party and it may
prohibit redistribution even inside a private build. P0 records the question and
P3 must answer it before shipping the original typography.

**The NIB set may not cover every screen.** The bundle holds 17 NIB files while
the class dump names far more view controllers, so some layouts exist only in
code. P0 reports the gap, and P3 recovers those layouts by decompilation.

## Dependencies created for later sub-projects

P1 consumes nothing from P0 directly, so the two can proceed in parallel once
this specification is approved.

P3 consumes all five P0 outputs. The asset catalog supplies the artwork, the
layout reports supply geometry, and the PieMenu analysis supplies the capture
wheel. A P3 fidelity claim that no P0 output supports is a claim the project
cannot make.


## Corrections

This section records what this specification got wrong, so that a reader trusts
the corrected values rather than rediscovering the errors.

**The asset counts were arithmetic, not measurement.** The original table stated
259 paired and 28 single-resolution. Those numbers came from computing
`546 - 259 * 2`, which assumes every retina asset has a standard-resolution
partner. Twenty-eight assets carry a device suffix and break that assumption.
Three different counts circulated before the rule above was written down. The
values in the table now come from the manifest the tooling produces.

**The geometry encoding was assumed rather than read.** The specification
described `UIBounds` as a string of the form `{{0, 0}, {320, 44}}`. The artifact
never uses that form. The first implementation therefore matched nothing and
recovered zero geometry from all 1115 view nodes, while every test passed
because the tests supplied synthetic strings. An adversarial audit found it by
checking the tool against the artifact instead of against its own tests.

**Repeated property keys were dropped.** The original `resolve()` wrote each
value into a dictionary keyed by property name. Keys repeat inside a single
object's value window, so 620 of 4229 values vanished, and every array holding
more than one element collapsed to its last element. The parser now emits an
ordered list and asserts that the emitted count equals the count the header
declares.

**The layout reports now carry 120 frames, 67 of them at a non-zero origin.**
Before the correction, every view printed at `(0, 0)`.
