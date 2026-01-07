import sys
sys.path.append("../")

from graphs.cfg import ControlFlowGraph
from util import get_construct, get_line, get_id
from criteria.node_coverage import NodeCoverage

source = open("./index.py").read()
cfg = ControlFlowGraph(source)
nc = NodeCoverage(cfg)

for node in cfg.nodes():
    print(get_construct(node), get_line(node), get_id(node))

print(nc.test())
