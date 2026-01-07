import sys
sys.path.append("../")

from graphs.cfg import ControlFlowGraph
from util import get_construct, get_line, get_id

source = open("./index.py").read()
st = ControlFlowGraph(source)

for node in st.nodes():
    print(get_construct(node), get_line(node), get_id(node))

dfs = st.dfs()
bfs = st.bfs()

print("\ndfs")
for (n1, n2) in dfs:
    print(get_construct(n1), get_line(n1), get_id(n1))
    print(get_construct(n2), get_line(n2), get_id(n2))

print("\nbfs")
for (n1, n2) in bfs:
    print(get_construct(n1), get_line(n1), get_id(n1))
    print(get_construct(n2), get_line(n2), get_id(n2))
