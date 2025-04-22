# Usage of Knowledge Graphs in Data Structures
# Knowledge Graphs are a way to represent information in a structured format, allowing for better organization and retrieval of data.
from rdflib import Graph, URIRef, Literal, Namespace, RDF

#Create a new graph
graph = Graph()
#print(graph.serialize(format="turtle").decode("utf-8"))

#Define namespace prefixes
ex=Namespace("http://example.org/")
print(ex)

#Add triples to the graph
graph.add((ex.alice, ex.knows, ex.bob))
graph.add((ex.bob, ex.knows, ex.charlie))
graph.add((ex.alice, ex.age, Literal(25)))
graph.add((ex.bob, ex.age, Literal(30)))
graph.add((ex.charlie, ex.age, Literal(35)))

#Query the graph
print("People Alice Knows:")
for person in graph.objects(ex.alice, ex.knows):
    print(person)

print("\n People and their Ages:")
for person, age in graph.subject_objects(ex.age):
    print(f"{person} is {age} years old")
print("\nKnowledge Graph:")

#Serialize the graph to a string (in Turtle format)
print(graph.serialize(format="turtle"))

#Serialize the graph to a file (in Turtle format)
with open("Knowledge_Graph.ttl","w") as file:
    file.write(graph.serialize(format="turtle"))