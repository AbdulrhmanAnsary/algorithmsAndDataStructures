#!/usr/bin/env python

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def add_root(self, root_value):
    root = Node(root_value)
    return root

  def has_two_children(self, parent:Node) -> bool:
    return parent.left != None and parent.right != None

  def is_leaf(self, node:Node) -> bool:
    return node.left is None and node.right is None

  def add_child(self, parent, child_value, extend=True):
    if self.has_two_children(parent) and not extend:
      raise OverflowError("OverflowError: The parent  has already reached the maximum number of children")
    elif parent.left == None:
      parent.left = Node(child_value)
      return parent.left
    elif parent.right == None:
      parent.right = Node(child_value)
      return parent.right
    else:
      if parent.left:
        self.add_child(parent.left, child_value)
      else:
         self.add_child(parent.right, child_value)

  def add_list(self, parent:Node, values:list):
    for item in values:
      self.add_child(parent, item)

  def print_tree(self, parent, prefix="", is_left=True):
    """print tree using pre-order algorithm"""
    if parent != None:
      print(prefix, ("|-- " if is_left else "\-- "), parent.data, sep="")
      prefix += "│   " if is_left else "    "
      self.print_tree(parent.left, prefix)
      self.print_tree(parent.right, prefix, False)

try:
  tree = BinaryTree()
  root = tree.add_root(1)
  left_root = tree.add_child(root, 2)
  right_root = tree.add_child(root, 3)
  tree.add_child(root, 4)
  tree.add_child(root, 5)
  tree.add_child(root, 6)
  tree.add_child(root, 7)
  tree.print_tree(root)
  print("====================================")
  nums = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
  tree.add_list(root, nums)
  tree.print_tree(root)
  print("====================================")
  list = [77, 78, 79, 80, 81, 82, 83, 79, 90]
  tree.add_list(right_root, list)
  tree.print_tree(root)
except OverflowError as OE:
  print(OE)
