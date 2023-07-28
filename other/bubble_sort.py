def bubble_sort(lst):
    for pass_num in range(len(lst) - 1, 0, -1):
        for i in range(pass_num):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
    return lst


# modified


def short_bubble(lst):
    exchanges = True
    N = len(lst) - 1

    while N > 0 and exchanges:
        exchanges = False
        for i in range(N):
            if lst[i] > lst[i + 1]:
                exchanges = True
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        N -= 1
    return lst
