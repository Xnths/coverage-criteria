# Node Coverage Criteria

This criteria checks if all nodes in the control flow graph were visited.

Formally, for a set of Test requirements (TR), the node coverage criteria is defined as:

$$
TR = \set{visit(n) : \forall n \in N}
$$

Where $visit(n)$ is a boolean function that returns true if the node $n$ was visited and false otherwise.

A test $t \in TR$ satisfies the node coverage criteria if and only if $visit(n) = true$ for all $n \in N$.

# Detection

The node coverage criteria is a necessary condition for the program to be correct.

It detects
- Dead code
- Unreachable logic
- Infinite loops
- Missing initialization
- Gross structural defects (unused functions, variables, etc...)

# Getting Started

To run the node coverage criteria, you need to have Python 3.8 or higher installed.

```bash
python -m node_coverage test.py
```