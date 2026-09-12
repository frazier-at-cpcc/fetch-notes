// DumpListing.java - print the disassembly listing for an address range.
//
// The decompiler is a convenience, not the record. Several claims in the
// geometry document rest on instruction detail that the decompiler discards or
// gets wrong: an if-then-else block whose second arm is Thumb-2 predication, a
// return value built from a movt immediate rather than a literal pool word, and
// the constants inside two Objective-C block bodies that Ghidra's analyzer left
// in ARM mode. This script prints the instructions themselves so that a reader
// confirms those claims inside Ghidra rather than reaching for a second
// disassembler.
//
// Usage, one or more start:end pairs, both ends inclusive:
//   analyzeHeadless <proj_dir> CatchP0 -process Catch -noanalysis \
//     -scriptPath tools/ghidra -postScript DumpListing.java 000636b2:000636e0
//
// An odd start address means the range is Thumb code, which is the same
// convention the binary itself uses for a Thumb entry point. The script then
// clears the range, sets the TMode context register, and disassembles before
// listing. Ghidra's auto analysis leaves the two icon layout block bodies in
// ARM mode, so those two ranges need the odd form:
//   ... -postScript DumpListing.java 00065729:00065786 00065821:0006586e
//
// Addresses are Ghidra addresses, which equal the file offset plus 0x1000 in
// this binary.

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.lang.Register;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;

import java.math.BigInteger;

public class DumpListing extends GhidraScript {

    private Address addr(long v) {
        return currentProgram.getAddressFactory().getAddress(Long.toHexString(v));
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length == 0) {
            println("no ranges given, expected start:end");
            return;
        }
        for (String range : args) {
            String[] ends = range.split(":");
            long startVal = Long.parseLong(ends[0].replace("0x", ""), 16);
            long endVal = Long.parseLong(ends[ends.length - 1].replace("0x", ""), 16);
            boolean thumb = (startVal & 1L) != 0;
            Address start = addr(startVal & ~1L);
            Address end = addr(endVal & ~1L);

            println("");
            println("===== LISTING " + start + " to " + end
                    + (thumb ? " (forced Thumb)" : "") + " =====");

            if (thumb) {
                Register tmode = currentProgram.getProgramContext().getRegister("TMode");
                clearListing(start, end);
                currentProgram.getProgramContext().setValue(tmode, start, end, BigInteger.ONE);
                disassemble(start);
            } else if (currentProgram.getListing().getInstructionAt(start) == null) {
                disassemble(start);
            }

            InstructionIterator it = currentProgram.getListing().getInstructions(start, true);
            while (it.hasNext()) {
                Instruction ins = it.next();
                if (ins.getAddress().compareTo(end) > 0) break;
                StringBuilder bytes = new StringBuilder();
                for (byte b : ins.getBytes()) {
                    bytes.append(String.format("%02x", b));
                }
                println(String.format("%s  %-12s  %s", ins.getAddress(), bytes, ins.toString()));
            }
        }
        println("=== DONE ===");
    }
}
