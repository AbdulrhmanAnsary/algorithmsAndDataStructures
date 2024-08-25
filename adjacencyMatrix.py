#!/usr/bin/env python

class Graph:
  def __init__(self, num_vertices):
    self.num_vertices = num_vertices
    self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

  def add_edge(self, vertex1, vertex2):
    self.adjacency_matrix[vertex1][vertex2] = 1
    self.adjacency_matrix[vertex2][vertex1] = 1

  def print_graph(self):
    for row in self.adjacency_matrix:
      print(row)

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.print_graph()

