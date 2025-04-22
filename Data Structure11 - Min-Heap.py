#Python implementation of a Min-Heap data structure. A min-heap is a complete binary tree where the value of each node is less than or equal to the values of its children. It is commonly used for priority queues, heap sort, and Dijkstra's algorithm.
class MinHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def parent(self, index):
        # Return the parent index of a given index
        return (index - 1) // 2

    def left_child(self, index):
        # Return the left child index of a given index
        return 2 * index + 1

    def right_child(self, index):
        # Return the right child index of a given index
        return 2 * index + 2

    def insert(self, key):
        """
        Insert a new key into the heap.
        """
        # Add the key to the end of the heap
        self.heap.append(key)
        # Heapify-up to maintain the min-heap property
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        """
        Heapify-up to restore the min-heap property after insertion.
        """
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # Swap the current node with its parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            # Move up to the parent index
            index = self.parent(index)

    def extract_min(self):
        """
        Extract and return the minimum element from the heap.
        """
        if not self.heap:
            return None  # Heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element in the heap

        # Replace the root (minimum) with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Heapify-down to restore the min-heap property
        self.heapify_down(0)
        return root

    def heapify_down(self, index):
        """
        Heapify-down to restore the min-heap property after extraction.
        """
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find the smallest among the current node and its children
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def get_min(self):
        """
        Get the minimum element from the heap without removing it.
        """
        if not self.heap:
            return None
        return self.heap[0]

    def display(self):
        """
        Display the heap as a list.
        """
        print(self.heap)


# Example Usage
if __name__ == "__main__":
    min_heap = MinHeap()

    # Insert elements into the heap
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)
    min_heap.insert(2)

    # Display the heap
    print("Heap:")
    min_heap.display()

    # Get the minimum element
    print("\nMinimum element:", min_heap.get_min())

    # Extract the minimum element
    print("\nExtracted minimum:", min_heap.extract_min())

    # Display the heap after extraction
    print("\nHeap after extraction:")
    min_heap.display()