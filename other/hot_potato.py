from queue import Queue


def hot_potato(namelist, num):
    q = Queue()

    for member in namelist:
        q.enqueue(member)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()




