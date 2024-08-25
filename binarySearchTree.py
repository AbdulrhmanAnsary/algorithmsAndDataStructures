#!/usr/bin/python

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  root = None
  left = None
  right = None
  nodes_count = 0

  def has_two_children(self, parent:Node):
    return parent.left != None and parent.right != None

  def add_root(self, root_value):
    self.root = Node(root_value)
    self.nodes_count += 1
    return self.root

  def insert_node(self, parent, child_value, extend=True):
    if self.has_two_children(parent) and not extend:
      raise OverflowError("OverflowError: The parent has already reached the maximum number of children")
    elif self.root is None:
      raise RuntimeError("RuntimeError: There is no root to add child")
    # Add left to the root
    elif self.left is None and child_value < self.root.data:
      parent.left = Node(child_value)
      self.left = parent.left
      self.nodes_count += 1
      return parent.left
    # Add right to the root
    elif self.right is None:
      parent.right = Node(child_value)
      self.right = parent.right
      self.nodes_count += 1
      return parent.right
    # Adding a child to the appropriate branch (left/right)
    elif parent.left is None and child_value < parent.data:
      parent.left = Node(child_value)
      self.nodes_count += 1
      return parent.left
    elif parent.right is None and child_value >= parent.data:
      parent.right = Node(child_value)
      self.nodes_count += 1
      return parent.right
    else:
      if parent.left and child_value < self.root.data:
        self.insert_node(parent.left, child_value)
      else:
        self.insert_node(parent.right, child_value)

  def add_list(self, parent:Node, values:list):
    for item in values:
      self.insert_node(parent, item)

  def print_tree(self, parent, prefix="", is_left=True):
    """print tree using pre-order algorithm"""
    if parent != None:
      print(prefix, "|-- " if is_left else "/-- ", parent.data, sep="")
      prefix += "|   " if is_left else "    "
      self.print_tree(parent.left, prefix)
      self.print_tree(parent.right, prefix, False)

  def _print_tree_in_order(self, parent):
    if parent is None:
      return []
    return self._print_tree_in_order(parent.left) + [parent.data] + self._print_tree_in_order(parent.right)

  def print_tree_in_order(self, parent):
    in_order_list = self._print_tree_in_order(parent)
    print(in_order_list)

try:
  tree = BinarySearchTree()
  root = tree.add_root(10)
  tree.insert_node(root, 1)
  tree.insert_node(root, 10)
  tree.insert_node(root, 7)
  tree.insert_node(root, 9)
  tree.insert_node(root, 5)
  tree.print_tree(root)
  print("Nodes count: ", tree.nodes_count)
  print("=============================")
  nums = [37, 38, 39, 40, 41, 42, 43, 10, 4, 9, 100]
  tree.add_list(root, nums)
  tree.print_tree(root)
  print("Nodes count: ", tree.nodes_count)
  print("=============================")
  tree.print_tree_in_order(root)
except OverflowError as OE:
  print(OE)
except RuntimeError as RE:
  print(RE)
