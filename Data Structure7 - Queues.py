# Queue Class Definition
class Queue: 
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def display(self):
        print("Front ->", self.queue, "<-Rear")

if __name__ == "__main__":
    # Create a queue instance
    queue = Queue()

    # Enqueue items
    queue.enqueue("John")
    queue.enqueue("James")
    queue.enqueue("Jim")
    queue.enqueue("Ron")
    queue.enqueue("Tom")
    queue.enqueue("Sam")

    # Display the queue
    queue.display()

    # Dequeue an item
    print("Dequeued:", queue.dequeue())

    # Display the queue again
    queue.display()
    # Check the size of the queue
    print("Size of the queue:", queue.size())
    print("Is the queue empty?", queue.is_empty())

    # Check if the queue is empty
    while (queue.is_empty()==False):
        print("Dequeued:", queue.dequeue())
        # Display the queue again
        queue.display()
        # Check the size of the queue
        print("Size of the queue:", queue.size())