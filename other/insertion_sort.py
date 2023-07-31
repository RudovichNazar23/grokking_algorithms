
def insertion_sort(lst):
    for index in range(1, len(lst)):

        curr_value = lst[index]
        pos = index

        while pos > 0 and lst[pos - 1] > curr_value:
            lst[pos] = lst[pos - 1]
            pos -= 1
        lst[pos] = curr_value
    return lst
