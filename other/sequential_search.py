def sequential_search(lst, item):
    pos = 0
    found = False

    while pos < len(lst) and not found:
        if lst[pos] == item:
            found = True
        else:
            pos += 1
    return found


# But if array is sorted

def ordered_sequential_search(lst, item):
    ind = 0
    found = False
    stop = False

    while ind < len(lst) and not found and not stop:
        if lst[ind] == item:
            found = True
        else:
            if lst[ind] > item:
                stop = True
            else:
                ind += 1
    return found

