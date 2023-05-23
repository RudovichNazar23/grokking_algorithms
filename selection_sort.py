
def selection_sort(lst: list):
    N = len(lst)

    for i in range(0, N - 1):
        minimal_value = lst[i]
        minimal_index = i

        for x in range(i + 1, N):
            if minimal_value > lst[x]:
                minimal_value = lst[x]
                minimal_index = x

        if not minimal_index == i:
            t = lst[i]
            lst[i] = lst[minimal_index]
            lst[minimal_index] = t


