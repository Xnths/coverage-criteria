import ast
import networkx as nx

class ControlFlowGraph:
    def __init__(self, source: str):
        self._graph = nx.DiGraph()
        self.source = source
        self.tree = ast.parse(source)
        self.terminal = object()
        self._graph.add_node(self.terminal)
        self._build()

    def _build(self):
        body = self.tree.body
        if not body:
            self._graph.add_edge(self.terminal, self.terminal)
            return
        self._build_block(body, self.terminal)

    def _build_block(self, stmts, next_stmt):
        prev = None

        for stmt in stmts:
            self._graph.add_node(stmt)

            if prev is not None:
                self._graph.add_edge(prev, stmt)

            if isinstance(stmt, ast.FunctionDef):
                if stmt.body:
                    self._graph.add_edge(stmt, stmt.body[0])
                    self._build_block(stmt.body, next_stmt)
                prev = stmt

            elif isinstance(stmt, ast.If):
                if stmt.body:
                    self._graph.add_edge(stmt, stmt.body[0])
                    self._build_block(stmt.body, next_stmt)
                if stmt.orelse:
                    self._graph.add_edge(stmt, stmt.orelse[0])
                    self._build_block(stmt.orelse, next_stmt)
                else:
                    if next_stmt is not None:
                        self._graph.add_edge(stmt, next_stmt)
                prev = None

            elif isinstance(stmt, ast.While):
                if stmt.body:
                    self._graph.add_edge(stmt, stmt.body[0])
                    self._build_block(stmt.body, stmt)
                if next_stmt is not None:
                    self._graph.add_edge(stmt, next_stmt)
                prev = None

            elif isinstance(stmt, ast.For):
                if stmt.body:
                    self._graph.add_edge(stmt, stmt.body[0])
                    self._build_block(stmt.body, stmt)
                if next_stmt is not None:
                    self._graph.add_edge(stmt, next_stmt)
                prev = None

            elif isinstance(stmt, ast.Return):
                self._graph.add_edge(stmt, self.terminal)
                prev = None

            else:
                prev = stmt

        if prev is not None and next_stmt is not None:
            self._graph.add_edge(prev, next_stmt)

    def nodes(self) -> set:
        return set(self._graph.nodes)

    def edges(self) -> set:
        return set(self._graph.edges)

    def dfs(self) -> list:
        return list(nx.dfs_edges(self._graph, self.tree.body[0]))

    def bfs(self) -> list:
        return list(nx.bfs_edges(self._graph, self.tree.body[0]))

    def sccs(self) -> list:
        return list(nx.strongly_connected_components(self._graph))

    def loop_sccs(self) -> list:
        loops = []
        for c in self.sccs():
            if len(c) > 1:
                loops.append(c)
            else:
                v = next(iter(c))
                if self._graph.has_edge(v, v):
                    loops.append(c)
        return loops

    def infinite_loop_sccs(self) -> list:
        entry = self.tree.body[0]
        reachable = nx.descendants(self._graph, entry) | {entry}
        infinite = []

        for c in self.loop_sccs():
            if not c & reachable:
                continue
            exits = False
            for v in c:
                for _, w in self._graph.out_edges(v):
                    if w not in c:
                        exits = True
            if not exits:
                infinite.append(c)

        return infinite
