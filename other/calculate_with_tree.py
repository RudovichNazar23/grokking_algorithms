import operator

from stack import Stack
from trees import BinaryTree


def build_parse_tree(expr: str):
    tokens = expr.split()
    prev_stack = Stack()
    tree = BinaryTree("")
    prev_stack.push(tree)

    current_tree = tree

    for i in tokens:
        if i == "(":
            current_tree.insert_left("")
            prev_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ["*", "/", "+", "-", ")"]:
            current_tree.set_roo_value(int(i))
            parent = prev_stack.pop()
            current_tree = parent
        elif i in ["*", "/", "+", "-"]:
            current_tree.set_roo_value(i)
            current_tree.insert_right("")
            prev_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = prev_stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(parseTree: BinaryTree):
    opers = {
        "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv
    }

    left = parseTree.get_left_child()
    right = parseTree.get_right_child()

    if left and right:
        fn = opers[parseTree.get_root_value()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parseTree.get_root_value()


expression = "( 3 * ( 5 + 3 ) )"

# print(evaluate(build_parse_tree(expression)))

