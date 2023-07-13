from unordered_list import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item: Node):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() < item.get_data():
                previous = current
                current = current.get_next()
            else:
                stop = True
        if previous is None:
            item.set_next(self.head)
            self.head = item
        else:
            item.set_next(current)
            previous.set_next(item)

    def remove(self, item):
        current = self.head
        found = False
        previous = None

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
            return found
        else:
            previous.set_next(current.get_next())
            return found

    def search(self, item: int):
        current = self.head
        stop = False
        found = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        counter = 0

        while current is not None:
            current = current.get_next()
            counter += 1
        return counter

    def index(self, item):
        current = self.head
        counter = 0

        while current is not None:
            if current.get_data() == item:
                return counter
            else:
                current = current.get_next()
                counter += 1
        return counter

    def pop(self):
        current = self.head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()

    def pop_from_position(self, pos):
        current = self.head
        counter = 0
        previous = None

        while current.get_next() is not None and counter != pos:
            previous = current
            current = current.get_next()
        if previous is None:
            previous = self.head.get_next()
            self.head = previous
            return current.get_data()
        else:
            previous.set_next(current.get_next())
            return current.get_data()


