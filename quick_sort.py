def q_sort(lst: list):
    if len(lst) < 2:
        return lst
    else:
        elem = lst[0]

        less = [
            i for i in lst[1:] if i <= elem
        ]

        greater = [
            i for i in lst[1:] if i > elem
        ]

        return q_sort(less) + [elem] + q_sort(greater)
