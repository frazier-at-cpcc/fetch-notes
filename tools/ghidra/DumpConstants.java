// Prints a literal pool address as a raw word, a float, and a double.
//
// The geometry constants are PC-relative literal pool entries, so the
// decompiler shows them as DAT_ labels rather than values. Ghidra addresses are
// NOT file offsets in this binary; they sit 0x1000 above them. Reading the
// bytes through Ghidra memory rather than seeking in the file is what keeps a
// mis-mapped offset from producing a plausible but wrong constant.
//
// Usage, from the repository root:
//   export JAVA_HOME=/opt/homebrew/Cellar/openjdk@21/<version>/libexec/openjdk.jdk/Contents/Home
//   "$(brew --prefix ghidra)/libexec/support/analyzeHeadless" \
//     build/ghidra_proj CatchP0 -process Catch -noanalysis \
//     -scriptPath tools/ghidra -postScript DumpConstants.java 00063740 00063748 0006374c
//
// With no arguments it reads the three pathForSliceSegment constants.
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;

public class DumpConstants extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] addrs = getScriptArgs();
        if (addrs.length == 0) {
            addrs = new String[] {"00063740", "00063748", "0006374c"};
        }
        println("=== LITERAL POOL CONSTANTS ===");
        for (String a : addrs) {
            Address ad = currentProgram.getAddressFactory().getAddress(a);
            byte[] b4 = new byte[4];
            byte[] b8 = new byte[8];
            currentProgram.getMemory().getBytes(ad, b4);
            int bits = ((b4[3] & 0xff) << 24) | ((b4[2] & 0xff) << 16)
                     | ((b4[1] & 0xff) << 8) | (b4[0] & 0xff);
            float f = Float.intBitsToFloat(bits);
            String dbl = "n/a";
            try {
                currentProgram.getMemory().getBytes(ad, b8);
                long lo = 0;
                for (int i = 7; i >= 0; i--) lo = (lo << 8) | (b8[i] & 0xffL);
                dbl = Double.toString(Double.longBitsToDouble(lo));
            } catch (Exception e) { /* fewer than 8 readable bytes */ }
            println(String.format("%s  raw=%02x%02x%02x%02x  float=%s  double=%s",
                a, b4[0], b4[1], b4[2], b4[3], Float.toString(f), dbl));
        }
        println("=== DONE ===");
    }
}
