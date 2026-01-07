import ast
import networkx as nx

class ControlFlowGraph:
    def __init__(self, source: str):
        self._graph = nx.DiGraph()
        self.source = source
        self.tree = ast.parse(source)
        self._build()

    def _build(self):
        body = self.tree.body
        if not body:
            return
        self._build_block(body, None)

    def _build_block(self, stmts, next_stmt):
        prev = None

        for stmt in stmts:
            self._graph.add_node(stmt)

            if prev is not None:
                self._graph.add_edge(prev, stmt)

            if isinstance(stmt, ast.FunctionDef):
                if stmt.body:
                    self._graph.add_edge(stmt, stmt.body[0])
                    self._build_block(stmt.body, None)
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
