# Ghidra scripts

Four headless scripts that recover the capture wheel constants from the armv7
executable inside the pinned IPA. They exist so that the repository regenerates
`research/piemenu-geometry.md` rather than describing an analysis that lived in
throwaway files.

| Script | Reads |
|---|---|
| `DumpPieMenu.java` | Locates the PieMenu symbols and decompiles the geometry methods |
| `DumpConstants.java` | Prints a literal pool address as a raw word, a float, and a double |
| `DumpFunctions.java` | Decompiles a raw address, which is the only way to reach an Objective-C block body |
| `DumpListing.java` | Prints instructions, which is the only way to read Thumb-2 predication and `movt` immediates |

Every script carries its own usage comment at the top of the file.
`research/piemenu-geometry.md` holds the full procedure, including the import
step, the exact argument lists that produced each table, and the three Ghidra
behaviors that a reader needs to know before trusting decompiler output.

Run every command from the repository root. Ghidra resolves a bare script name
against the working directory before it searches `-scriptPath`, so a run started
from a directory that holds a same-named script loads that copy instead.
