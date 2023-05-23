def sum(lst: list):
    if not lst:
        return 0
    else:
        return lst[0] + sum(lst[1:])
