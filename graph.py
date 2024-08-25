#!/usr/bin/env python

from collections import deque

class Node:
  def __init__(self, data):
    self.data = data
    self.adjacency_list = []


class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_value):
    if vertex_value not in self.vertices:
      new_node = Node(vertex_value)
      self.vertices[vertex_value] = new_node
    else:
      raise RuntimeError(f"VertexDuplicateError: The vertex '{vertex_value}' already exists")

  def are_they_related(self, vertex1, vertex2):
    """vertex1, vertex2: The values of these vertices"""
    if vertex1 in self.vertices and vertex2 in self.vertices:
      return vertex2 in self.vertices[vertex1].adjacency_list
    else:
      raise RuntimeError(f"ElementNotFoundError: The vertex '{vertex1}' or '{vertex2}' does not exist")

  def add_edge(self, vertex1, vertex2):
    """vertex1, vertex2: The values of these vertices"""
    if not self.are_they_related(vertex1, vertex2):
      self.vertices[vertex1].adjacency_list.append(self.vertices[vertex2])
      self.vertices[vertex2].adjacency_list.append(self.vertices[vertex1])
    else:
      raise RuntimeError(f"EdgeError: The vertices '{vertex1}' and '{vertex2}' are already related")

  def depth_first_search(self, target):
    """It used depth first search algorithm to find the target and return a node"""
    if target not in self.vertices:
      raise RuntimeError(f"ElementNotFoundError: The vertex '{target}' does not exist")

    visited_vertices = set()
    for vertex in self.vertices:
      if vertex == target:
        return self.vertices[vertex]
      if vertex in visited_vertices:
        continue
      visited_vertices.add(vertex)
      dfs_result = self._depth_first_search(vertex, target, visited_vertices)
      if dfs_result:
        return dfs_result
    return None

  def _depth_first_search(self, start_vertex, target, visited_vertices):
    """Helper recursive DFS function."""
    if start_vertex == target:
      return self.vertices[start_vertex]
    visited_vertices.add(start_vertex)
    for edge in self.vertices[start_vertex].adjacency_list:
      if edge.data not in visited_vertices:
        result = self._depth_first_search(edge.data, target, visited_vertices)
        if result:
          return result
    return None

  def breadth_first_search(self, target):
    """It used breadth first search algorithm to find the target and return a node"""
    if target not in self.vertices:
      raise RuntimeError(f"ElementNotFoundError: The vertex '{target}' does not exist")

    visited_vertices = set()
    queue = deque()

    # Start with all vertices in the graph
    for vertex in self.vertices:
      if vertex == target:
        return self.vertices[vertex]
      if vertex in visited_vertices:
        continue
      visited_vertices.add(vertex)
      queue.append(self.vertices[vertex])

      while queue:
        current_node = queue.popleft()
        if current_node.data == target:
          return current_node
        for edge in current_node.adjacency_list:
          if edge.data == target:
            return edge
          if edge.data not in visited_vertices:
            visited_vertices.add(edge.data)
            queue.append(edge)
    return None

  def print_graph(self):
    for vertex in self.vertices:
      print(f"{vertex}: ", end="")
      for edge in self.vertices[vertex].adjacency_list:
        print(edge.data, end=" ")
      print()


try:
  graph = Graph()
  graph.add_vertex("a")
  graph.add_vertex("b")
  graph.add_vertex("c")
  graph.add_vertex("d")
  graph.add_vertex("e")
  graph.add_edge("a", "b")
  graph.add_edge("a", "c")
  graph.add_edge("a", "e")
  graph.add_edge("b", "d")
  graph.add_edge("c", "b")
  graph.add_edge("c", "d")
  graph.print_graph()
  print(graph.breadth_first_search("d").data)
except RuntimeError as RE:
  print(RE)
