#!/bin/python

def bubble_sort(list):
  for _ in range(len(list)):
    for i in range(len(list) - 1):
      if list[i+1] < list[i]:
        list[i], list[i+1] = list[i+1], list[i]

nums = [10, 7, 5, 1, 5, 12, 9]

print(nums)
print("After sorting:")
bubble_sort(nums)
print(nums)
