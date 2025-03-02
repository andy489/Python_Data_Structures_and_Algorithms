class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return f"{self.value}"


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(4)
my_queue.enqueue(2)
my_queue.dequeue()
my_queue.print_queue()
