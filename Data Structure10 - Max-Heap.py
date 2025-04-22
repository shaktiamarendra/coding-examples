#Python implementation of a Max-Heap data structure. A max-heap is a complete binary tree where the value of each node is greater than or equal to the values of its children. This structure is commonly used for priority queues and heap sort.
class MaxHeap:
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
        # Heapify-up to maintain the max-heap property
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        """
        Heapify-up to restore the max-heap property after insertion.
        """
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            # Swap the current node with its parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            # Move up to the parent index
            index = self.parent(index)

    def extract_max(self):
        """
        Extract and return the maximum element from the heap.
        """
        if not self.heap:
            return None  # Heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element in the heap

        # Replace the root (maximum) with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Heapify-down to restore the max-heap property
        self.heapify_down(0)
        return root

    def heapify_down(self, index):
        """
        Heapify-down to restore the max-heap property after extraction.
        """
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Find the largest among the current node and its children
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is not the current node, swap and continue heapifying down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def get_max(self):
        """
        Get the maximum element from the heap without removing it.
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
    max_heap = MaxHeap()

    # Insert elements into the heap
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(30)

    # Display the heap
    print("Heap:")
    max_heap.display()

    # Get the maximum element
    print("\nMaximum element:", max_heap.get_max())

    # Extract the maximum element
    print("\nExtracted maximum:", max_heap.extract_max())

    # Display the heap after extraction
    print("\nHeap after extraction:")
    max_heap.display()