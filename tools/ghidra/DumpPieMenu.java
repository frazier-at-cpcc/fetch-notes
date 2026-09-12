// Locates the PieMenu symbols and decompiles the three geometry methods.
//
// Usage, from the repository root:
//   export JAVA_HOME=/opt/homebrew/Cellar/openjdk@21/<version>/libexec/openjdk.jdk/Contents/Home
//   "$(brew --prefix ghidra)/libexec/support/analyzeHeadless" \
//     build/ghidra_proj CatchP0 -process Catch -noanalysis \
//     -scriptPath tools/ghidra -postScript DumpPieMenu.java
//
// Takes no arguments. Import the binary first with -import and
// -processor ARM:LE:32:v7; this script assumes an analyzed program.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.symbol.Symbol;
import ghidra.program.model.symbol.SymbolIterator;
import ghidra.util.task.ConsoleTaskMonitor;

import java.util.ArrayList;
import java.util.List;

public class DumpPieMenu extends GhidraScript {

    private static final String[] TARGETS = {
        "pathForSliceSegment", "layoutIconViews", "pathAnimationWithDuration"
    };

    private boolean isTarget(String name) {
        for (String t : TARGETS) {
            if (name.contains(t)) return true;
        }
        return false;
    }

    @Override
    public void run() throws Exception {
        println("=== SYMBOLS CONTAINING PieMenu ===");
        SymbolIterator syms = currentProgram.getSymbolTable().getAllSymbols(true);
        int symCount = 0;
        while (syms.hasNext()) {
            Symbol s = syms.next();
            String n = s.getName();
            if (n.contains("PieMenu") || isTarget(n)) {
                println(s.getAddress() + "  " + n);
                symCount++;
            }
        }
        println("symbols matched: " + symCount);

        println("");
        println("=== FUNCTIONS CONTAINING PieMenu OR A TARGET SELECTOR ===");
        List<Function> hits = new ArrayList<>();
        FunctionIterator fns = currentProgram.getFunctionManager().getFunctions(true);
        while (fns.hasNext()) {
            Function f = fns.next();
            String n = f.getName();
            if (n.contains("PieMenu") || isTarget(n)) {
                hits.add(f);
                println(f.getEntryPoint() + "  " + n);
            }
        }
        println("functions matched: " + hits.size());

        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        ConsoleTaskMonitor mon = new ConsoleTaskMonitor();

        for (Function f : hits) {
            if (!isTarget(f.getName())) continue;
            println("");
            println("===== DECOMPILE " + f.getName() + " @ " + f.getEntryPoint() + " =====");
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
