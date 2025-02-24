class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def print_list(self):  # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pretty_print_list(self):  # O(n)
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        print("None")

    def append(self, value):  # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):  # O(n)
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):  # O(1)
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):  # O(1)
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):  # O(n)
        if self.head is None:
            return None
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):  # O(n)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):  # O(n)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):  # O(n)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        prev = self.get(index - 1)
        if prev is None or prev == self.tail:
            return None

        to_remove = prev.next
        prev.next = prev.next.next
        to_remove.next = None
        self.length -= 1
        return to_remove

    def reverse_recursive(self):  # O(n)
        def dfs(node):
            node_next = node.next
            if node_next != self.tail:
                dfs(node_next)
            node_next.next = node

        if self.head == self.tail:
            return

        # flip arrows
        dfs(self.head)
        # switch head and tail
        self.head.next = None
        new_tail = self.head
        self.head = self.tail
        self.tail = new_tail

    def reverse(self):  # O(n)
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next  # traverse
            temp.next = before  # flip
            # catching up
            before = temp
            temp = after


my_linked_list = LinkedList(1)

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
my_linked_list.print_list()

my_linked_list.reverse_recursive()

my_linked_list.print_list()
