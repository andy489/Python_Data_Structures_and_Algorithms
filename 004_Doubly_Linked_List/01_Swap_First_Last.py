class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last_nodes(self):
        if self.length <= 1:
            return None
        if self.length == 2:
            memo_head = self.head
            self.head = self.tail
            self.head.prev = None

            memo_head.next = None
            memo_head.prev = self.head
            self.head.next = memo_head

            return None

        # Detach head
        memo_head = self.head
        self.head = self.head.next
        self.head.prev = None
        memo_head.next = None
        memo_head.prev = None

        # Detach tail
        memo_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        memo_tail.next = None
        memo_tail.prev = None

        # Re-attach head
        memo_tail.next = self.head
        self.head.prev = memo_tail
        # Update head
        self.head = self.head.prev

        # Re-attach tail
        memo_head.prev = self.tail
        self.tail.next = memo_head
        # Update tail
        self.tail = self.tail.next

    # Swap only values
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head.value, self.tail.value = self.tail.value, self.head.value


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1
"""
