# Python program to demonstrate the tree traversal techniques
# using DFS and BFS
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
    
    def generate_tree(self, node, data):
        if node.left is None:
            node.left = Node(data)
        elif node.right is None:
            node.right = Node(data)
        else:
            print("Both children are already present")
            self.generate_tree(node.left, data)
        return self

#Display the family tree
def display_tree(node, level=0):
    if node is not None:
        print(' ' * level + '->', node.data)
        display_tree(node.left, level + 1)
        display_tree(node.right, level + 1)

def DFS(node, data, recursion_counter=0):
    if node is not None:
        if node.data == data:
            print(f"Found Node at Recursion Counter: {recursion_counter}")
            return True
        return DFS(node.left, data, recursion_counter + 1) or DFS(node.right, data, recursion_counter + 1)
    print(f"Node with data '{data}' not found after {recursion_counter} recursions")
    return False

def BFS(node, data, steps_counter=0):
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        steps_counter += 1
        if current.data == data:
            print(f"Found Node at Steps Counter: {steps_counter}")
            return True
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False

#Create the family tree
tree_root = Node("John")
tree_root.generate_tree(tree_root, "Alice")
tree_root.generate_tree(tree_root, "Bob")
tree_root.generate_tree(tree_root, "Emily")
tree_root.generate_tree(tree_root, "Mark")
tree_root.generate_tree(tree_root, "Sarah")
tree_root.generate_tree(tree_root, "Tom")
tree_root.generate_tree(tree_root, "Ron")

#Display the family tree
display_tree(tree_root)

#Display the family tree using DFS
print("\nDFS Traversal:")
print(f"John is present in tree: , {DFS(tree_root, 'John')}")
print(f"Sarah is present in tree: , {DFS(tree_root, 'Sarah')}")
print(f"Ten is present in tree: , {DFS(tree_root, 'Ten')}")

#Display the family tree using BFS
print("\nBFS Traversal:")
print(f"John is present in tree:  {BFS(tree_root, 'John')}")
print(f"Sarah is present in tree:  {BFS(tree_root, 'Sarah')}")
print(f"Ten is present in tree: {BFS(tree_root, 'Ten')}")