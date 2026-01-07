import ast

class SyntaxTree:
    def __init__(self, source: str):
        self.source = source
        self.tree = ast.parse(source)

    def nodes(self) -> set:
        root = self.tree.body[0]
        nodes = set()

        for node in ast.walk(root):
            nodes.add(node)
        return nodes

    def edges(self) -> set:
        root = self.tree.body[0]
        edges = set()

        for parent in ast.walk(root):
            for child in ast.iter_child_nodes(parent):
                edges.add((parent, child))
        return edges