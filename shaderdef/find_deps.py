import ast

class _FindDepsVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self):
        super(_FindDepsVisitor, self).__init__()
        self.inputs = set()
        self.outputs = set()

    def visit_Attribute(self, node):
        if node.value.id == 'self':
            if isinstance(node.ctx, ast.Load):
                self.inputs.add(node.attr)
            elif isinstance(node.ctx, ast.Store):
                self.outputs.add(node.attr)


def find_deps(node):
    """Find attributes of "self"."""
    fdv = _FindDepsVisitor()
    fdv.visit(node)
    return fdv