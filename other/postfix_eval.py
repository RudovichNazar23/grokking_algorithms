from stack import Stack


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfix_eval(postfix_exp_string: str):
    stack = Stack()

    tokens = postfix_exp_string.split()

    operators = "*/+-"

    for token in tokens:
        if token.isdigit():
            num = int(token)
            stack.push(num)
        elif token in operators:
            num2 = stack.pop()
            num1 = stack.pop()
            result = doMath(token, num1, num2)
            stack.push(result)
    return stack.pop()


