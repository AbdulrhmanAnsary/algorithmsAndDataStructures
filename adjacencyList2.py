class Graph:
  def __init__(self):
    self.adjacency_list = {}

  def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = []

  def add_edge(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)

  def print_graph(self):
    for vertex in self.adjacency_list:
      print(f"{vertex}: {self.adjacency_list[vertex]}")

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()

