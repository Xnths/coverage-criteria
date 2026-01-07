
import sys
sys.path.append("../")

from graphs.cfg import ControlFlowGraph
from util import get_construct, get_line, get_id

source = open("./index.py").read()
st = ControlFlowGraph(source)

for node in st.nodes():
    print(get_construct(node), get_line(node), get_id(node))
