from stack import Stack


def balanced_brackets_checker(s: str):
    stack = Stack()

    index = 0
    balanced = True

    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        index += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False

# common case


def match(open ,close):
    open_brackets = "([{"
    close_brackets = ")]}"

    return open_brackets.index(open) == close_brackets.index(close)


def balance_checker(s: str):
    stack = Stack()

    index = 0
    balanced = True

    while index < len(s):
        symbol = s[index]

        if symbol in "([{":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                t = stack.pop()
                if not match(t, symbol):
                    balanced = False
        index += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


