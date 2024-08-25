#!/bin/python

class StackUnderflowError(Exception):
  message = "StackUnderflowError: The stack is empty"
  def __init__(self):
    super().__init__(self.message)

class Stack:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if self.isEmpty():
      raise StackUnderflowError()
    return self.stack.pop()

  def display(self):
    print(self.stack[::-1])

  def top(self):
    if self.isEmpty():
      raise StackUnderflowError()
    return self.stack[-1]

try:
  nums = Stack()

  nums.push(5)
  nums.push(10)
  nums.push(15)
  nums.push(20)
  nums.push(25)
  nums.pop()
  nums.pop()
  nums.display()
  print(nums.top())
except StackUnderflowError as e:
  print(e)
