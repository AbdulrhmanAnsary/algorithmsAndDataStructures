#!/usr/bin/env python

# The code is from an arabic channel called litprog

def adjacency_list(array_size, edges):
  graph = [[] for i in range(array_size)]

  for edge in edges:
    a = edge[0]
    b = edge[1]
    graph[a].append(b)
    graph[b].append(a)
  return graph

array_size = 5
edges = [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3)]

print(adjacency_list(array_size, edges))
