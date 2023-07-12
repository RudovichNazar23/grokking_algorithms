class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, value):
        self.data = value

    def set_next(self, value):
        self.next = value


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # insert item to be the first item of the list
    def add(self, obj: Node):
        obj.set_next(self.head)
        self.head = obj

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, value):
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, obj):
        current = self.head
        last_elem = None

        while current is not None:
            last_elem = current
            current = current.get_next()
        last_elem.set_next(obj)

    def insert(self, obj: Node, index: int):
        current = self.head
        previous = None
        counter = 0

        while counter < index:
            previous = current
            current = current.get_next()
            counter += 1
        previous.set_next(obj)
        obj.set_next(current)

    def index(self, item):
        current = self.head
        counter = 0

        while current is not None:
            if current.get_data() == item:
                return counter
            else:
                current = current.get_next()
                counter += 1
        return None

    def pop(self, index=-1):
        current = self.head
        counter = 0
        previous = None

        if index == 0:
            previous = self.head.get_data()
            self.head = current.get_next()
            return previous

        elif index == -1:
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            return current.get_data()
        else:
            while current.get_next() is not None and counter < index:
                previous = current
                current = current.get_next()
                counter += 1
            previous.set_next(current.get_next())
            return current.get_data()






