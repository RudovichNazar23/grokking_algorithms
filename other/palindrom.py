from deque import Deque


def palindrom_check(st: str):
    char_deque = Deque()

    for i in st:
        char_deque.addRear(i)

    result = True

    while char_deque.size() > 1 and result:
        first = char_deque.removeFront()
        last = char_deque.removeRear()

        if not first == last:
            result = False

    return result


print(palindrom_check("mama"))
