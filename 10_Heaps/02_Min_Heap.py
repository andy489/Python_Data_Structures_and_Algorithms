class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] < self.heap[min_index]):
                min_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] < self.heap[min_index]):
                min_index = right_index

            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value


min_heap = MinHeap()
min_heap.insert(12)
min_heap.insert(10)
min_heap.insert(8)
min_heap.insert(6)
min_heap.insert(4)
min_heap.insert(2)

print(min_heap.heap)  # [2, 6, 4, 12, 8, 10]

removed = min_heap.remove()
print(f'Removed: {removed}, Heap: {min_heap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = min_heap.remove()
print(f'Removed: {removed}, Heap: {min_heap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = min_heap.remove()
print(f'Removed: {removed}, Heap: {min_heap.heap}')  # Removed: 6, Heap: [8, 12, 10]

"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]
"""
