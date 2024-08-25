#!/bin/python

class QueueUnderflowError(Exception):
  message = "QueueUnderfloeError: The queue is empty"
  def __init__(self):
    super().__init__(self.message)

class Queue:
  def __init__(self):
    self.queue = []

  def isEmpty(self):
    return len(self.queue) == 0

  def enqueue(self, value):
    self.queue.append(value)

  def dequeue(self):
    if self.isEmpty():
      raise QueueUnderflowError()
    self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      raise QueueUnderflowError()
    return self.queue[0]

  def display(self):
    print(self.queue)

try:
  nums = Queue()

  nums.enqueue(5)
  nums.enqueue(10)
  nums.enqueue(15)
  nums.enqueue(20)
  nums.enqueue(25)
  nums.dequeue()
  nums.dequeue()
  nums.enqueue(30)
  print(nums.peek())
  nums.display()
except QueueUnderflowError as e:
  print(e)
