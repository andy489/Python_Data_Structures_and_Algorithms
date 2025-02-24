class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


def flip_arrows_between(start_node, end_node):
    def dfs(start: Node, end: Node):
        node_next = start.next
        if node_next != end:
            dfs(node_next, end)
        node_next.next = start

    if start_node == end_node:
        return

    # flip arrows
    dfs(start_node, end_node)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between_dfs(self, start_index, end_index):  # O(n)
        if start_index == end_index:
            return

        temp = self.head
        start_prev_node = None
        i = 0
        while i < start_index:
            start_prev_node = temp
            temp = temp.next
            i += 1
        start_node = temp
        while i < end_index:
            temp = temp.next
            i += 1
        end_node = temp

        end_node_next = end_node.next
        flip_arrows_between(start_node, end_node)
        if start_index > 0:
            start_prev_node.next = end_node
        else:
            self.head = end_node
        start_node.next = end_node_next

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return

        dummy_node = Node(0)
        dummy_node.next = self.head

        previous_node = dummy_node

        for i in range(start_index):
            previous_node = previous_node.next

        current_node = previous_node.next

        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move

        self.head = dummy_node.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
"""
