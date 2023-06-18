class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


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

