
var = [
    *range(0, 1000)
]


def binary_search(lst: list, item):
    min_value = 0
    max_value = len(lst) - 1

    while min_value <= max_value:
        mid = (min_value + max_value) // 2

        if mid == item:
            return item

        elif mid > item:
            max_value = mid - 1
        else:
            min_value = mid + 1
    return None


