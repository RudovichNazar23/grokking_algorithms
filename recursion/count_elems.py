def count(lst: list):
    if not lst:
        return 0
    else:
        return 1 + count(lst[1:])

