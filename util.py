def get_construct(node) -> str:
    return getattr(node, "__class__", None).__name__

def get_line(node) -> int:
    return getattr(node, "lineno", None)

def get_column(node) -> int:
    return getattr(node, "col_offset", None)

def get_end_line(node) -> int:
    return getattr(node, "end_lineno", None)

def get_end_column(node) -> int:
    return getattr(node, "end_col_offset", None)

def get_fields(node) -> tuple:
    return getattr(node, "_fields", ())

def get_context(node) -> str:
    ctx = getattr(node, "ctx", None)
    return ctx.__class__.__name__ if ctx is not None else None

def get_id(node) -> str:
    return getattr(node, "id", None)

def get_argument_name(node) -> str:
    return getattr(node, "arg", None)

def get_function_name(node) -> str:
    return getattr(node, "name", None)

def get_attribute_name(node) -> str:
    return getattr(node, "attr", None)

def get_constant_value(node):
    return getattr(node, "value", None)

def get_operator(node) -> str:
    op = getattr(node, "op", None)
    return op.__class__.__name__ if op is not None else None

def get_comparison_operators(node) -> tuple:
    ops = getattr(node, "ops", None)
    if ops is None:
        return ()
    return tuple(op.__class__.__name__ for op in ops)

def get_number_of_children(node) -> int:
    return sum(1 for _ in ast.iter_child_nodes(node))
