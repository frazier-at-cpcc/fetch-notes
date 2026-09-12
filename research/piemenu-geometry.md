# Capture Wheel Geometry

Recovered constants for the Catch Notes 5.2.8 capture wheel, the radial menu the
application presents from the capture button. Every value below comes from the
armv7 executable inside the pinned IPA, MD5 `9a891d439c74198cfa32e39a37e6bb34`.

Two independent toolchains produced this document. The first pass used
`otool -arch armv7 -tV` plus throwaway annotation scripts. The second pass used
Ghidra 12.1.3 headless and the four scripts committed under `tools/ghidra/`.
Where the two passes agreed, the row below says so. Where they disagreed, the
**Disagreements** section names the constant, the third derivation that settled
it, and the value that won.

Every address in this document is the address that both `otool` and Ghidra
print. The corresponding file offset is `0x1000` lower. The bytes at file offset
`0x62680` are `f0 b5 03 af 84 b0 90 1e`, which is the function entry that both
tools place at `0x63680`.

## Provenance labels

Every row in every table carries a **Provenance** label. The label is one of the
six values below and nothing else. A row labelled **not recovered** is a result.
An unlabelled guess is a defect that reaches P3 as an untraceable fidelity bug.

| Label | Meaning |
|---|---|
| read directly (Ghidra) | Ghidra read the value out of program memory or out of an instruction, and the `otool` pass did not report it |
| read directly (otool) | The `otool` pass read the value out of the instruction stream, and the Ghidra pass did not reach it |
| confirmed by both | Both toolchains read the same value independently |
| computed | Arithmetic over values that were read, with no unread term |
| estimated | An inference that no read value pins down |
| not recovered | The analysis did not reach the value |

A reimplementation that matches a **computed** value carries the same evidence as
one that matches a read value, because every term was read. A reimplementation
that matches an **estimated** value carries no evidence of matching the original.

## Reproducing this document

The first pass depended on throwaway scripts that lived under `build/`, which git
ignores, so nothing in the repository regenerated it. The Ghidra scripts under
`tools/ghidra/` close that gap. A reader who supplies the IPA reruns every
instruction-level claim below with the four commands in this section.

The analysis machine ran Ghidra 12.1.3 and OpenJDK 21.0.12.1 from Homebrew.
Adjust the two paths for another installation.

```bash
export JAVA_HOME=/opt/homebrew/Cellar/openjdk@21/21.0.12.1/libexec/openjdk.jdk/Contents/Home
GHIDRA=/opt/homebrew/Cellar/ghidra/12.1.3/libexec/support/analyzeHeadless

# 1. Unpack the bundle. The binary lands at build/Payload/Catch.app/Catch.
tools/run_p0.sh path/to/Catch.ipa

# 2. Import and analyze once. The binary is a thin armv7 Mach-O, so Ghidra
#    selects the processor without help. This step takes several minutes.
"$GHIDRA" build/ghidra_proj CatchP0 -import build/Payload/Catch.app/Catch

# 3. Locate and decompile the geometry methods.
"$GHIDRA" build/ghidra_proj CatchP0 -process Catch -noanalysis \
  -scriptPath tools/ghidra -postScript DumpPieMenu.java

# 4. Read the literal pool entries that those methods load.
"$GHIDRA" build/ghidra_proj CatchP0 -process Catch -noanalysis \
  -scriptPath tools/ghidra -postScript DumpConstants.java \
  00063740 00063748 0006374c 00064fb0 00064fb8 00064fc0 00064fc8 00064fcc
```

Two further scripts reach what `DumpPieMenu.java` does not. `DumpFunctions.java`
decompiles an address, which is the only way to read an Objective-C block body,
because a block invoke function carries no symbol. `DumpListing.java` prints
instructions, which is the only way to read a Thumb-2 predicated instruction or a
`movt` immediate, because the decompiler discards both.

```bash
# The icon placement block and the contracted layout block.
"$GHIDRA" build/ghidra_proj CatchP0 -process Catch -noanalysis \
  -scriptPath tools/ghidra -postScript DumpFunctions.java 00064de8 00065084

# The slice edge trim, the TRIGGER_SIZE return value, and the two icon
# radius blocks. An odd start address forces Thumb decoding.
"$GHIDRA" build/ghidra_proj CatchP0 -process Catch -noanalysis \
  -scriptPath tools/ghidra -postScript DumpListing.java \
  000636b2:000636e0 000633f8:000633fe 00065729:00065786 00065821:0006586e
```

Run every command from the repository root. Ghidra resolves a bare script name
against the working directory before it searches `-scriptPath`, so a run started
from a directory that holds a same-named script loads that copy instead.

## Disagreements between the two derivations

Five claims differed between the first pass and the second. Each one received a
third derivation. The winner and the reason appear below. No value was adopted
quietly.

### 1. Slice count, five against eight

The second pass reported eight slices, from 360 divided by the 45 degree sweep.
The first pass reported five. The third derivation read four separate sites in
Ghidra, and all four agree on five.

`chooseSegment:` at `0x6386c` accepts an argument when `argument - 2` is below
the immediate 5. `segmentForPoint:` at `0x634f8` runs a counter from 2 and
returns 0 once the counter passes the immediate 6. `initWithFrame:` at `0x627a8`
builds slice layers in a loop that starts at 2 and exits at 7. The same method
builds divider spokes in a loop that starts at 1 and exits at 5, which draws four
spokes, and four spokes separate five slices.

**Five wins.** The wheel draws five of the eight slices that a 45 degree sweep
would allow. The arithmetic was the error, and this is the error class that the
provenance column exists to catch.

### 2. Unit of the slice edge trim, radians against degrees

The second pass called the 0.25 trim a degree value. The first pass called it a
radian value. The third derivation read the instruction order at `0x636b2`
through `0x636de`. The method converts both boundary angles from degrees to
radians with `vcvt.f32.f64` at `0x636c2` and `0x636c6`, and only then adds the
trim at `0x636d0` and `0x636de`.

**Radians wins.** The trim is 0.25 radians, which is a little over 14 degrees,
not a quarter of a degree. A reimplementation that treats it as degrees produces
slice edges that differ from the original by more than 14 degrees.

### 3. Scope of the negative trim, one segment against every segment

The second pass reported that segment 6 takes the positive trim and every other
segment takes the negative trim. The first pass reported that only segment 2
takes the negative trim. The third derivation printed the instructions with
`DumpListing.java`.

```
000636ca  04d1          bne 0x000636d6
000636cc  c5ef100f      vmov.f32 d16,#0x3e800000
000636d0  00ef200d      vadd.f32 d0,d0,d16
000636d4  05e0          b 0x000636e2
000636d6  022a          cmp r2,#0x2
000636d8  04bf          itt eq
000636da  c5ff100f      vmov.f32 d16,#0xbe800000
000636de  01ef201d      vadd.f32 d1,d1,d16
```

**Segment 2 only wins.** The second arm compares against 2 and guards both
floating point instructions with an `itt eq` block. The Ghidra decompiler emitted
the negative arm as an unconditional statement with a discarded result, which is
how the second pass lost the predicate. Segments 3, 4, and 5 receive no trim at
all.

### 4. Slice fill color, channel order reversed

The first pass recorded the slice fill color as red 0.27450981, green 0.65882355,
and blue 0.90588236, a blue. The Ghidra decompilation of `initWithFrame:` lists
the same three magnitudes in the opposite order. The third derivation read the
argument registers at the call site at `0x630c4`. Register `r2` carries
`0x3f67e7e8`, register `r3` carries `0x3f28a8a9`, the first stack word carries
`0x3e8c8c8d`, and the second carries `0x3f000000`.

**The Ghidra order wins.** Red is 0.9058823585510254, green is 0.658823549747467,
blue is 0.27450981736183167, and alpha is 0.5. The slice fill is a warm amber,
not a blue.

### 5. Origin of the 142.0 radius

The first pass labelled the construction radius **read directly** and then
derived it from four terms. Both halves of that row were wrong as stated, and the
value survives.

The slice construction radius is computed. `initWithFrame:` passes
`TRIGGER_SIZE * 0.5 + 114.0 + 10.0 - 22.0` to `pathForSliceSegment:` for each
slice layer. Every term was read, so the row is **computed**, not read directly.

Separately, the divider spokes in the same method read a stored double 142.0 at
`0x62b80` and use it as the spoke length without arithmetic. That row is **read
directly (Ghidra)**. The computed radius and the stored spoke length agree, which
is a cross-check rather than a single reading.

### Note on TRIGGER_SIZE, a toolchain limit rather than a disagreement

The Ghidra decompiler renders `+[PieMenu TRIGGER_SIZE]` as a return of an
uninitialized register and recovers no value. The method is three instructions,
and `DumpListing.java` prints them.

```
000633f8  0020          movs r0,#0x0
000633fa  c4f2a020      movt r0,#0x42a0
000633fe  7047          bx lr
```

`0x42A00000` is 80.0. Both toolchains reach the value once the listing replaces
the decompiler, so the row reads **confirmed by both**.

## Shared constants

Three values recur across the methods and appear once here rather than in every
table.

| Constant | Value | Provenance |
|---|---|---|
| `+[PieMenu TRIGGER_SIZE]` return value | 80.0 points | confirmed by both |
| Degree to radian factor | 0.017453292519943295 | confirmed by both |
| Slice sweep | 45.0 degrees | confirmed by both |

The degree to radian factor is stored three times as a double, at `0x63740` for
the slice path, at `0x62b78` for the divider spokes, and at `0x64fb8` for the
icon placement. The sweep is stored three times as a float, at `0x63748`,
`0x62b6c`, and `0x64fc8`. Each copy reads 45.0.

## Slice geometry

Method: `+[PieMenu pathForSliceSegment:withCenterPoint:radius:]`, implementation
at `0x63680`.

The method subtracts 2 from the segment index, multiplies the result by the
sweep, adds the start angle, converts both boundary angles from degrees to
radians, applies the edge trim, and calls
`+[UIBezierPath bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:]`
with `clockwise` set to 1. It then calls `addLineToPoint:` with the center point,
which closes the arc into a wedge.

| Constant | Value | Provenance |
|---|---|---|
| Segment index offset | 2 | confirmed by both |
| Sweep per slice | 45.0 degrees, float at `0x63748` | confirmed by both |
| Start angle for slice index 0 | -202.5 degrees, float at `0x6374c` | confirmed by both |
| Slice count | 5, covering segments 2 through 6 | confirmed by both |
| End-angle trim, segment 6 only | +0.25 radians, immediate `0x3e800000` | confirmed by both |
| Start-angle trim, segment 2 only | -0.25 radians, immediate `0xbe800000` | confirmed by both |
| Trim for segments 3, 4, and 5 | none | read directly (Ghidra) |
| Arc direction | clockwise, immediate 1 | confirmed by both |
| Path closure | `addLineToPoint:` to the center point, so no inner radius is stored | confirmed by both |
| Slice construction radius | 142.0 points | computed |
| Hit-test radius | 154.0 points | computed |

The construction radius is `TRIGGER_SIZE * 0.5 + 114.0 + 10.0 - 22.0`, read at
`0x62f56`, `0x62fc0`, `0x62f6c`, and `0x62f7e`. The hit-test radius is
`TRIGGER_SIZE * 0.5 + 114.0`, where the 114.0 is a separate stored double at
`0x63678` that `segmentForPoint:` loads. The hit region therefore extends 12.0
points beyond the drawn slice, and a reimplementation that uses one radius for
both purposes diverges from the original.

The boundary angles that follow from the start angle and the sweep are listed
below, before the trim. The values are normalized into the range 0 through 360
degrees for readability. The binary stores the negative form.

| Segment | Start | End | Center | Provenance |
|---|---|---|---|---|
| 2 | 157.5 | 202.5 | 180.0 | computed |
| 3 | 202.5 | 247.5 | 225.0 | computed |
| 4 | 247.5 | 292.5 | 270.0 | computed |
| 5 | 292.5 | 337.5 | 315.0 | computed |
| 6 | 337.5 | 22.5 | 0.0 | computed |

Segment 1 is not a slice. `segmentForPoint:` tests it first, by building
`+[UIBezierPath bezierPathWithOvalInRect:]` over `[[self innerCircle] frame]` and
sending `containsPoint:`. Segment 1 is therefore the center trigger, and its
region is the inner circle view rather than a computed radius. A return value of
0 means the point fell outside every region.

`-[PieMenu UIBezierPathForContentMask]` at `0x63494` is a separate path. It
returns `+[UIBezierPath bezierPathWithOvalInRect:]` over a rectangle with origin
`(0.0, 2.0)` and size `TRIGGER_SIZE` by `TRIGGER_SIZE`, so the content mask is an
80.0 point circle displaced 2.0 points down. The mask does not participate in hit
testing.

| Constant | Value | Provenance |
|---|---|---|
| Content mask origin | 0.0, 2.0 | confirmed by both |
| Content mask size | `TRIGGER_SIZE` square | confirmed by both |
| Divider spoke length | 142.0 points, double at `0x62b80` | read directly (Ghidra) |
| Divider spoke origin | 160.0, 160.0, double at `0x62b88` | read directly (Ghidra) |
| Divider spoke count | 4 | read directly (Ghidra) |
| Divider spoke stroke width | 3.0 points, then 1.0 point for the second layer | read directly (Ghidra) |
| Background disc frame | 320.0 square | read directly (Ghidra) |
| Background disc oval | inset 18.0, diameter 284.0 | read directly (Ghidra) |
| Background disc fill | white 0.9490196108818054, alpha 1.0 | read directly (Ghidra) |

## Icon placement

Method: `-[PieMenu layoutIconViewsWithRadius:iconScale:]`, implementation at
`0x64c8c`. The method sends `enumerateObjectsUsingBlock:` to `iconViews`. The
block invoke function sits at `0x64de8` and holds every constant.

The block captures a `__block` float that accumulates the placement angle in
degrees. The outer method initializes that variable to 180.0. The block reads the
accumulator, places the icon, and then adds 45.0 to the accumulator on every
path. Two indices bypass the accumulator to avoid a conversion rounding step.
Index 0 uses the double literal for pi at `0x64fb0`. Index 4 uses the double 0.0
at `0x64fc0`, which equals the 360.0 the accumulator would otherwise hold.

Each icon center is `center.x + radius * cos(angle)` and
`center.y + radius * sin(angle)`, where `center` is `[[self innerCircle] center]`
and `radius` is the method argument. The block then applies a per-index pixel
nudge, rounds both coordinates with `roundf`, and sends `setCenter:` and
`setBounds:`.

| Constant | Value | Provenance |
|---|---|---|
| Initial accumulator angle | 180.0 degrees, immediate `0x43340000` | confirmed by both |
| Accumulator increment per icon | 45.0 degrees, float at `0x64fc8` | confirmed by both |
| Angle for icon index 0 | 3.141592653589793 radians, double at `0x64fb0` | confirmed by both |
| Angle for icon index 4 | 0.0 radians, double at `0x64fc0` | confirmed by both |
| Placement center | `[[self innerCircle] center]` | confirmed by both |
| Placement radius | the `radius` argument, no internal proportion applied | confirmed by both |
| Icon base edge length | 56.0 points, float at `0x64fcc`, multiplied by `iconScale` | confirmed by both |
| Coordinate rounding | `roundf` on both axes | confirmed by both |
| Icon count | 5 | read directly (Ghidra) |
| Angular offset that centers an icon in its slice | 22.5 degrees past the slice start | computed |
| Mapping from icon index to segment index | icon index plus 2 | estimated |

The angular offset is half the read sweep of 45.0 degrees. The icon angles are
180.0, 225.0, 270.0, 315.0, and 0.0 degrees, and the slice centers computed from
`pathForSliceSegment:` are the same five values. The mapping from icon index to
segment index stays **estimated** because the two sequences match by value rather
than by a read association, and the analysis did not trace what populates
`iconViews` or in what order.

The block applies a fixed pixel nudge per icon index after computing the polar
position and before rounding. The nudges are asymmetric and do not follow from any
formula in the method.

| Icon index | X nudge | Y nudge | Provenance |
|---|---|---|---|
| 0 | +4.0 | -9.0 | confirmed by both |
| 1 | +1.0 | +1.0 | confirmed by both |
| 2 | +4.0 | +7.0 | confirmed by both |
| 3 | -3.0 | none emitted | confirmed by both |
| 4 | -9.0 | -7.0 | confirmed by both |

The radius argument itself is supplied by callers. Three call sites supply a value
built from `TRIGGER_SIZE`.

| Call site | Radius | Icon scale | Provenance |
|---|---|---|---|
| `-[PieMenu expandMenuAnimated:]`, non-animated path | `TRIGGER_SIZE * 0.5 + 62.70000076293945` | 1.0 | confirmed by both |
| Expand animation block at `0x65728` | `TRIGGER_SIZE * 0.5 + 62.70000076293945 + 7.5` | 1.0499999523162842 | confirmed by both |
| Settle animation block at `0x65820` | `TRIGGER_SIZE * 0.5 + 62.70000076293945` | 1.0 | confirmed by both |
| `-[PieMenu contractMenuAnimated:]`, non-animated path | `TRIGGER_SIZE * 0.5 + 62.70000076293945` | 1.0 | read directly (Ghidra) |

| Constant | Value | Provenance |
|---|---|---|
| Settled icon radius | 102.7 points | computed |
| Overshoot icon radius | 110.2 points | computed |

The addend reaches the code as a double, stored at `0x65720` for the non-animated
expand path, at `0x66100` for the non-animated contract path, and in the literal
pools of the two animation blocks. Every copy reads 62.70000076293945, which is
62.7 widened from a float. The sum is formed in double precision and narrowed to
a float before the call, so the float that reaches the method is 102.69999694824219
for the settled radius and 110.19999694824219 for the overshoot radius.

`-[PieMenu layoutIconViewsContracted]` at `0x65004` does not call this method. Its
block at `0x65084` sets every icon center to `[[self innerCircle] center]` and
every icon bounds to a 2.0 by 2.0 rectangle.

| Constant | Value | Provenance |
|---|---|---|
| Contracted icon center | `[[self innerCircle] center]` | confirmed by both |
| Contracted icon bounds | 2.0 by 2.0, immediate `0x40000000` | confirmed by both |

## Path animation

Method: `+[PieMenu pathAnimationWithDuration:timingFunctionName:fromPath:toPath:]`,
implementation at `0x64a90`.

The method builds a `CABasicAnimation` on key path `path`, sets the duration from
its float argument, sets the timing function from
`+[CAMediaTimingFunction functionWithName:]`, sets `fromValue` and `toValue` from
the two `CGPathRef` arguments, sets `removedOnCompletion` to `NO`, and sets
`fillMode` to `kCAFillModeForwards`.

| Constant | Value | Provenance |
|---|---|---|
| Animated key path | `@"path"` | confirmed by both |
| Animation class | `CABasicAnimation` | confirmed by both |
| `removedOnCompletion` | `NO` | confirmed by both |
| `fillMode` | `kCAFillModeForwards` | confirmed by both |
| Duration | supplied by the caller, no default in this method | confirmed by both |
| Timing function name | supplied by the caller, no default in this method | confirmed by both |

The method holds no duration of its own. Seven call sites supply one. The float
immediate appears beside each row because the decimal is the widened float rather
than the round number the author typed.

| Call site | Duration | Timing function | Provenance |
|---|---|---|---|
| `-[PieMenu expandMenuAnimated:]` | 0.15000000596046448 s, `0x3e19999a` | `kCAMediaTimingFunctionEaseInEaseOut` | confirmed by both |
| `-[PieMenu contractMenuQuicklyAnimated:]` | 0.10000000149011612 s, `0x3dcccccd` | `kCAMediaTimingFunctionEaseInEaseOut` | confirmed by both |
| `-[PieMenu contractMenuAnimated:]` | 0.07500000298023224 s, `0x3d99999a` | `kCAMediaTimingFunctionEaseInEaseOut` | confirmed by both |
| `-[PieMenu animationDidStop:finished:]`, expand correction, first site | 0.05000000074505806 s, `0x3d4ccccd` | `kCAMediaTimingFunctionEaseInEaseOut` | confirmed by both |
| `-[PieMenu animationDidStop:finished:]`, expand correction, second site | 0.05000000074505806 s, `0x3d4ccccd` | `kCAMediaTimingFunctionEaseInEaseOut` | confirmed by both |
| `-[PieMenu animationDidStop:finished:]`, contract correction, first site | 0.10000000149011612 s, `0x3dcccccd` | `kCAMediaTimingFunctionEaseOut` | confirmed by both |
| `-[PieMenu animationDidStop:finished:]`, contract correction, second site | 0.10000000149011612 s, `0x3dcccccd` | `kCAMediaTimingFunctionEaseOut` | confirmed by both |

The contract durations invert the naming. `contractMenuQuicklyAnimated:` runs a
0.1 second path animation and `contractMenuAnimated:` runs a 0.075 second one, so
the method named for speed animates the path for longer. A reimplementation that
swaps them to match the names would deviate from the original.

`animationDidStop:finished:` keys each animation by name, and the names identify
the phase.

| Animation key | Provenance |
|---|---|
| `animatePathExpandOvershoot` | confirmed by both |
| `animatePathExpandCorrect` | read directly (Ghidra) |
| `animatePathContractAnticipate` | read directly (Ghidra) |
| `animatePathContractCorrect` | read directly (Ghidra) |

Three `CAMediaTimingFunction` related symbols are reachable from these methods.
`kCAMediaTimingFunctionEaseInEaseOut` binds at `0x1F0740`,
`kCAMediaTimingFunctionEaseOut` binds at `0x1F0744`, and `kCAFillModeForwards`
binds at `0x1F0738`. No other named timing function appears in the bind table for
the PieMenu code paths.

| Constant | Value | Provenance |
|---|---|---|
| `kCAMediaTimingFunctionEaseInEaseOut` bind address | `0x1F0740` | confirmed by both |
| `kCAMediaTimingFunctionEaseOut` bind address | `0x1F0744` | confirmed by both |
| `kCAFillModeForwards` bind address | `0x1F0738` | confirmed by both |
| Any other named timing function in these paths | none | confirmed by both |

## Spring behavior

The expand sequence produces the spring. `-[PieMenu expandMenuAnimated:]` at
`0x65200` calls
`+[UIView animateWithDuration:delay:options:animations:completion:]` with a
duration read from `0x65718`, a delay of 0.0, and an options mask of 0. The
animation block drives the icons out to the overshoot radius at scale
1.0499999523162842. The completion block at `0x657a0` checks the `finished` flag
and, when it is set, calls `+[UIView animateWithDuration:animations:]` with a
duration read from `0x65818` to settle the icons back.

| Constant | Value | Provenance |
|---|---|---|
| Expand animation duration | 0.15000000596046448 s, double at `0x65718` | confirmed by both |
| Expand animation delay | 0.0 s | confirmed by both |
| Expand animation options mask | 0 | confirmed by both |
| Overshoot radius increment | +7.5 points, immediate at `0x6576e` | confirmed by both |
| Overshoot icon scale | 1.0499999523162842, immediate `0x3f866666` | confirmed by both |
| Settle animation duration | 0.05000000074505806 s, double at `0x65818` | confirmed by both |
| Settled icon scale | 1.0, immediate `0x3f800000` | confirmed by both |
| Settle gate | the `finished` flag of the completion block | confirmed by both |
| Transaction duration around the state change | 0.0 s, double at `0x65618` | read directly (Ghidra) |
| Expanded background color | black at alpha 0.3499999940395355 | read directly (Ghidra) |

The contract sequence mirrors the expand sequence.
`-[PieMenu contractMenuQuicklyAnimated:]` at `0x658a0` runs a UIView animation of
0.10000000149011612 seconds, read at `0x65ba8`. `-[PieMenu contractMenuAnimated:]`
at `0x65c40` runs one of 0.07500000298023224 seconds, read at `0x660f8`, and its
completion block at `0x66180` runs a further animation of 0.10000000149011612
seconds, read at `0x66208`, with an options mask of `0x20000`.

| Constant | Value | Provenance |
|---|---|---|
| Quick contract UIView duration | 0.10000000149011612 s, double at `0x65ba8` | read directly (Ghidra) |
| Contract UIView duration | 0.07500000298023224 s, double at `0x660f8` | read directly (Ghidra) |
| Contract completion duration | 0.10000000149011612 s, double at `0x66208` | read directly (Ghidra) |
| Contract completion options mask | `0x20000` | read directly (Ghidra) |

`+[PieMenu EXPANDED_RECT:]` at `0x6343c` returns
`CGRectInset([self TRIGGER_RECT], -argument, -argument)`. Two arguments reach it
from the animation paths.

| Constant | Value | Provenance |
|---|---|---|
| Resting mask inset argument | 114.0, immediate `0x42e40000` | read directly (Ghidra) |
| Overshoot mask inset argument | 124.0, immediate `0x42f80000` | read directly (Ghidra) |
| `TRIGGER_RECT` contents | | not recovered |
| Resting mask circle radius | 154.0 points | estimated |
| Overshoot mask circle radius | 164.0 points | estimated |

The two mask radii stay **estimated** because `CGRectInset` grows the rectangle
that `TRIGGER_RECT` returns, and this pass did not read `TRIGGER_RECT`. The
arithmetic holds only if that rectangle is the 80.0 point trigger square.

## Instance variable `_sprungOpen`

Declared at offset 92 as a `char`. The three sites below establish what the flag
records. It is set when a touch lands on the center trigger while the menu is
closed, cleared when the touch leaves the center trigger, and read at selection
time to decide whether the wheel collapses. The effect is that a press and release
on the center trigger leaves the wheel standing open.

`-[PieMenu beginTrackingWithTouch:withEvent:]` at `0x647b4` sets the flag. The
written value is 1 when the touched segment equals 1, the center trigger, and the
menu was not already expanded. The value is 0 in every other case.

`-[PieMenu continueTrackingWithTouch:withEvent:]` at `0x64928` clears the flag.
When `segmentForPoint:` returns anything other than 1, the method sends
`setSprungOpen:` with 0, so dragging off the center trigger cancels the spring.

`-[PieMenu chooseSegment:]` at `0x6386c` reads the flag. The method branches on the
argument first. For a slice, meaning segments 2 through 6, it unhighlights the
current segment, sets the highlighted segment to 0, calls
`contractMenuQuicklyAnimated:` without consulting the flag, and sends
`pieMenu:didChooseSlice:` to the delegate with the argument less 2. For segment 1
it unhighlights the current segment, sets the highlighted segment to 0, and returns
early when the menu is not expanded. When the menu is expanded the method reads
`sprungOpen`. A true flag returns without collapsing the wheel. A false flag falls
through to `[self contractMenuAnimated:[self osSupportsInteractionDuringAnimation]]`.

| Constant | Value | Provenance |
|---|---|---|
| Ivar offset | 92 | read directly (otool) |
| Ivar type | `char` | read directly (otool) |
| Set condition | touched segment equals 1 and the menu is not expanded | confirmed by both |
| Clear condition | `segmentForPoint:` returns a value other than 1 | confirmed by both |
| Effect when true | `chooseSegment:` returns without contracting | confirmed by both |
| Effect when false | `chooseSegment:` contracts the menu | confirmed by both |
| Slice index reported to the delegate | segment less 2 | read directly (Ghidra) |

The two ivar offsets come from the class metadata that `tools/objc_dump32.py`
decodes, not from the Ghidra pass, so both rows read **read directly (otool)**.

## Instance variable `_osSupportsInteractionDuringAnimation`

Declared at offset 93 as a `char`. The flag is a runtime operating system check,
and it is the animated flag passed to every expand and contract call.

`-[PieMenu initWithFrame:]` at `0x627a8` assigns it. The method reads
`[[UIDevice currentDevice] systemVersion]`, takes `floatValue`, compares the
result against the immediate `0x40a00000`, which is 5.0, and sends
`setOsSupportsInteractionDuringAnimation:` with the result of a
greater-than-or-equal test. The value is therefore 1 on iOS 5.0 and later and 0
on earlier systems. The binary states the threshold and the selector name. It does
not state which UIKit release the threshold tracks, so a reimplementation should
treat 5.0 as the recorded boundary rather than derive it from platform history.

The flag governs two distinct behaviors.

First, it is passed as the `animated` argument.
`-[PieMenu activateSegment:]` at `0x63750` calls
`expandMenuAnimated:[self osSupportsInteractionDuringAnimation]` and
`contractMenuAnimated:[self osSupportsInteractionDuringAnimation]`.
`-[PieMenu chooseSegment:]` at `0x6386c` passes the same value to
`contractMenuQuicklyAnimated:` on the slice-selection path and to
`contractMenuAnimated:` on the center-trigger path.

Second, it gates `stopAnimations`. Both `-[PieMenu expandMenuAnimated:]` and
`-[PieMenu contractMenuAnimated:]` reach a branch taken when the `animated`
argument is false. That branch reads the flag and calls `stopAnimations` only when
the flag is true. On a system that cannot deliver touches during animation, the
code leaves the in-flight animation alone.

| Constant | Value | Provenance |
|---|---|---|
| Ivar offset | 93 | read directly (otool) |
| Ivar type | `char` | read directly (otool) |
| Source | `[[[UIDevice currentDevice] systemVersion] floatValue] >= 5.0` | confirmed by both |
| Comparison threshold | 5.0, immediate `0x40a00000` | confirmed by both |
| Comparison operator | greater than or equal | confirmed by both |
| Primary use | the `animated` argument to every expand and contract call | read directly (otool) |
| Secondary use | gates `stopAnimations` on the non-animated branch | confirmed by both |
| UIKit release the threshold tracks | | not recovered |

## Not recovered

The rows below are open. They are recorded so that a later pass does not mistake
absence for completeness.

| Item | Provenance |
|---|---|
| `+[PieMenu TRIGGER_RECT]` contents | not recovered |
| `-[PieMenu layoutSubviews]` at `0x63e40`, the geometry for `_outerCircle`, `_innerCircle`, and `_innerCircleLip` | not recovered |
| `CircleView` geometry, including the source of its frame | not recovered |
| What populates `iconViews`, and in what order | not recovered |
| Highlighted and unhighlighted slice colors | not recovered |
| The path that the expand overshoot animates from | not recovered |
| The UIKit release behind the 5.0 threshold | not recovered |

One color was read in passing and is not part of this task. The call at `0x630c4`
inside the slice layer loop passes red 0.9058823585510254, green
0.658823549747467, blue 0.27450981736183167, and alpha 0.5 to
`+[UIColor colorWithRed:green:blue:alpha:]`. The three components equal 231, 168,
and 70 over 255. A later color pass should confirm this against the highlighted
and unhighlighted states rather than treat one call site as the whole palette.

| Constant | Value | Provenance |
|---|---|---|
| Slice layer fill color at `0x630c4` | red 0.9058823585510254, green 0.658823549747467, blue 0.27450981736183167, alpha 0.5 | confirmed by both |
| The rest of the wheel palette | | not recovered |

## Ghidra notes

Three behaviors of the toolchain shaped this pass and will shape the next one.

The decompiler drops Thumb-2 predication. An `itt` block reaches the output as an
unconditional statement whose result is discarded, which reverses the meaning of
the code. Any claim about a conditional constant needs the listing, which is what
`DumpListing.java` prints.

Auto analysis leaves some Objective-C block bodies in ARM mode. The two icon
layout blocks at `0x65728` and `0x65820` decompile to garbage until the `TMode`
context register is set over the range. `DumpListing.java` accepts an odd start
address and sets that register before disassembling, which is how the icon radius
and icon scale became readable.

The decompiler loses a return value that a method builds with `movt` alone, as
`TRIGGER_SIZE` does. The listing recovers it.
