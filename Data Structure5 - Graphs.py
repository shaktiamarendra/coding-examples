# Graph Class Definition
class Graph:
    def __init__(self):
        self.adjacency_list={}
    
    def add_vertex(self, vertex):
        self.adjacency_list[vertex]=[]
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
    
    def check_edge_exists(self, vertex1, vertex2):
        for vertex, neighbours in self.adjacency_list.items():
            if vertex1==vertex and vertex2 in neighbours:
                print(f"Success, {vertex1} and {vertex2} are connected")
                return True
        print(f"Failure, {vertex1} and {vertex2} are not connected")
        return False    

    def display(self):
        for vertex, neighbours in self.adjacency_list.items(): # .items() converts dictionary into a tuple
            print(vertex, "->", neighbours)

#Create an instance of the Graph
social_network=Graph()

#Add vertices
social_network.add_vertex('A')
social_network.add_vertex('B')
social_network.add_vertex('C')
social_network.add_vertex('D')
social_network.add_vertex('E')
social_network.add_vertex('F')

#Add edges
social_network.add_edge('A', 'B')
social_network.add_edge('A', 'C')
social_network.add_edge('B', 'D')
social_network.add_edge('B', 'E')
social_network.add_edge('C', 'E')
social_network.add_edge('C', 'F')
social_network.add_edge('E', 'F')

#Add edges
social_network.display()

# Check if edge exists
social_network.check_edge_exists('B', 'C')
social_network.check_edge_exists('F', 'E')