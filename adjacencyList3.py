class Node:
  def __init__(self, data):
    self.data = data
    self.edges = []  # List to store edges (connected nodes)

class Graph:
  def __init__(self):
    self.vertices = {}  # Dictionary to store nodes by their value

  def add_node(self, node_value):
    if node_value not in self.vertices:
      new_node = Node(node_value)
      self.vertices[node_value] = new_node

  def add_edge(self, vertice1, vertice2):
    if vertice1 in self.vertices and vertice2 in self.vertices:
      self.vertices[vertice1].edges.append(self.vertices[vertice2])
      self.vertices[vertice2].edges.append(self.vertices[vertice1])

  def print_graph(self):
    for vertice in self.vertices:
      print(f"{vertice}:", end=" ")
      for edge in self.vertices[vertice].edges:
        print(edge.data, end=" ")
      print()

# Usage
graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_node("d")
graph.add_node("e")
graph.add_edge("a", "b")
graph.add_edge("a", "c")
graph.add_edge("a", "d")
graph.add_edge("b", "d")
graph.add_edge("b", "c")
graph.add_edge("b", "e")
graph.add_edge("c", "e")
graph.add_edge("c", "d")
graph.add_edge("d", "e")
graph.print_graph()
