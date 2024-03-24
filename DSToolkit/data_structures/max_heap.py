class MaxHeap:

    '''
    A Max Heap is a complete binary tree where every node's value is greater than or equal to the values of
    its children, with operations to insert elements and extract the maximum element efficiently
    '''

    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        while self._left_child(index) < len(self.heap):
            largest = self._left_child(index)
            if (self._right_child(index) < len(self.heap) and
                    self.heap[self._right_child(index)] > self.heap[largest]):
                largest = self._right_child(index)

            if self.heap[largest] > self.heap[index]:
                self._swap(index, largest)
                index = largest
            else:
                break

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_max(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


# Example usage
heap = MaxHeap()
heap.insert(3)
heap.insert(2)
heap.insert(15)
heap.insert(5)
heap.insert(4)
heap.insert(45)


print(f"Max Heap: {heap}")
print(f"Extracted Max: {heap.extract_max()}")
print(f"After extraction: {heap}")
