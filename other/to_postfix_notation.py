from stack import Stack
from string import ascii_uppercase, digits


def to_postfix(value: str):
    costs = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    stack = Stack()

    res = []

    tokens = value.split()

    for token in tokens:
        if token in ascii_uppercase or token in digits:
            res.append(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            top = stack.pop()

            while top != "(":
                res.append(top)
                top = stack.pop()
        else:
            while not stack.is_empty() and costs[stack.peek()] >= costs[token]:
                res.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        res.append(stack.pop())
    return "".join(res)


