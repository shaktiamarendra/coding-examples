#Node Class Definition
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

#Linked List Class Definition
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_Node=Node(data)
        if self.head is None:
            self.head = new_Node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_Node

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Step 1: Create a new node
        new_node.next = self.head  # Step 2: Point new node to current head
        self.head = new_node  # Step 3: Update head to the new node
    
    def delete(self, data):
        if self.head is None:
            print("Error: Empty List")
            return
        
        current=self.head
        if data == current.data :
            print("Deleting Head Node")
            self.head=current.next
            return
        
        previous=current
        current=current.next
        counter=1
        # Traverse the list to find the node
        while current is not None:
            if current.data == data:
                previous.next=current.next
                print(f"Deleting Node at position {counter}")
                return
            previous=current
            current=current.next
            counter +=1
        print(f"Error: Node with value {data} not found")
    
    def displayLinks(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display(self):
        current = self.head
        count=0
        while current:
            print(f"Data at Position {count} is: {current.data}")
            current = current.next
            count +=1

# Create an instance of the linked list
my_list = LinkedList()

#Insert elements into the linked lits
while True:
    data=int(input("Please enter the new element in the linked list"))
    if data == 0 :
        break
    my_list.insert (data)

#Display the Linked List
my_list.display()
#Delete an element from the Linked List
del_num=int(input("Please enter the node to be deleted"))
my_list.delete(del_num)
#Add a node at the beginning
my_list.insert_at_beginning(454)
#Display the Linked List
my_list.displayLinks()