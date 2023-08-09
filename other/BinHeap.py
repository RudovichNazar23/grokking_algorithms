class BinHeap:
    def __init__(self):
        self.heap_list = [0, ]
        self.current_size = 0

    def __per_cup(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2

    def __perc_down(self, i):
        while i * 2 <= self.current_size:
            mc = self.min_child(i)

            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.__per_cup(self.current_size)

    def del_min(self, k):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.__perc_down(1)
        return ret_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0, ] + alist[:]
        while i > 0:
            self.__perc_down(i)
            i -= 1
