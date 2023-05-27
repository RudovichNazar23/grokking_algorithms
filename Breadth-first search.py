from collections import deque


class Worker:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job


me = Worker("John", "web-developer")

claire = Worker("Claire", "barber")

bob = Worker("Bob", "book-seller")

alice = Worker("Alice", "english_teacher")

johnny = Worker("johnny", "software_engineer")
anuj = Worker("anuj", "taxi_driver")
peggy = Worker("peggy", "poet")
tom = Worker("tom", "banana_seller")


graph = dict()

graph[me] = [claire, bob, alice]

graph[claire] = [tom, johnny]

graph[alice] = [peggy]

graph[bob] = [peggy, anuj]

graph[johnny] = []
graph[anuj] = []
graph[peggy] = []
graph[tom] = []


def is_banana_seller(job: str):
    return job == "banana_seller"


def search(person):
    search_queue = deque()
    search_queue += graph[person]

    searched = []

    while search_queue:
        worker = search_queue.popleft()

        if not worker in searched:
            if is_banana_seller(worker.job):
                return f"{worker.name} sells bananas"
            else:
                search_queue += graph[worker]
                searched.append(worker)

    return "I didn't manage to find a banana_seller...("


