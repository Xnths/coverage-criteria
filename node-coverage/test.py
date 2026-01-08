import sys
sys.path.append("../")

from graphs.cfg import ControlFlowGraph
from util import get_construct
from criteria.node_coverage import NodeCoverage

source = open("./index.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

print("Test is_even function")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")

print("Paths: ")
for path in nc.paths():
    for node in path:
        print(get_construct(node))
    print("\n")

print ("\n")

source = open("./dead_code.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

print("Test dead_code function. Here it must failed.")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")

source = open("./unreachable_logic.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

print("Test unreachable_logic function. Here it must failed.")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")

source = open("./infinite_loop.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

print("Test infinite_loop function. Here it must failed.")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")

source = open("./missing_initialization.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

print("Test missing_initialization function. Here it must failed.")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")

source = open("./gross_structural_defect.py").read()
cfg = ControlFlowGraph(source)
c = NodeCoverage(cfg)

print("Test gross_structural_defect function. Here it must failed.")
print("Passed: ", nc.test())
print("Coverage: ", nc.coverage())

print ("\n")