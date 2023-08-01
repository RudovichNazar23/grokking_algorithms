
def shell_sort(alist: list):
    sublist_count = len(alist) // 2

    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(alist, start_pos, sublist_count)
        sublist_count //= 2


def gap_insertion_sort(alist, start, gap):
    for index in range(start + gap, len(alist), gap):
        curr_val = alist[index]
        pos = index

        while pos > 0 and alist[pos - 1] > curr_val:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = curr_val


