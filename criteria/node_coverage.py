from graphs.cfg import ControlFlowGraph

class NodeCoverage:
    def __init__(self, cfg: ControlFlowGraph):
        self._cfg = cfg
        self._covered = set()
        self._total = set(cfg.nodes())

    def _cover(self, node):
        self._covered.add(node)

    def _is_covered(self, node):
        return node in self._covered

    def _successors(self, node):
        return {v for u, v in self._cfg.edges() if u == node}

    def _dfs(self, node):
        if self._is_covered(node):
            return
        self._cover(node)
        for child in self._successors(node):
            self._dfs(child)

    def test(self):
        root = self._cfg.tree.body[0]
        self._dfs(root)
        return self._covered == self._total

    def coverage(self):
        return len(self._covered) / len(self._total)
