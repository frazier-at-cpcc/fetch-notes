// DumpFunctions.java - decompile arbitrary addresses in the Catch binary.
//
// Named methods are reachable through DumpPieMenu.java. Objective-C block
// invoke bodies are not: they carry no symbol and the constants that place the
// icon views live inside them. This script takes raw addresses and decompiles
// whatever function contains each one, creating a function first when Ghidra's
// analysis left the address bare.
//
// Usage:
//   analyzeHeadless <proj_dir> CatchP0 -process Catch -noanalysis \
//     -scriptPath tools/ghidra -postScript DumpFunctions.java 00064de8 00065084
//
// Addresses are Ghidra addresses, which equal the file offset plus 0x1000 in
// this binary. Thumb entry points may be given with or without the low bit set.

import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.util.task.ConsoleTaskMonitor;

public class DumpFunctions extends GhidraScript {

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length == 0) {
            println("no addresses given");
            return;
        }

        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        ConsoleTaskMonitor mon = new ConsoleTaskMonitor();

        for (String a : args) {
            long v = Long.parseLong(a.replace("0x", ""), 16);
            v = v & ~1L; // a Thumb entry point carries the low bit set
            Address ad = currentProgram.getAddressFactory().getAddress(Long.toHexString(v));
            Function f = getFunctionContaining(ad);
            if (f == null) {
                f = createFunction(ad, null);
            }
            println("");
            if (f == null) {
                println("===== NO FUNCTION AT " + ad + " =====");
                continue;
            }
            println("===== DECOMPILE " + f.getName() + " @ " + f.getEntryPoint()
                    + " (requested " + ad + ") =====");
            DecompileResults res = decomp.decompileFunction(f, 180, mon);
            if (res.decompileCompleted()) {
                println(res.getDecompiledFunction().getC());
            } else {
                println("DECOMPILE FAILED: " + res.getErrorMessage());
            }
        }
        decomp.dispose();
        println("=== DONE ===");
    }
}
