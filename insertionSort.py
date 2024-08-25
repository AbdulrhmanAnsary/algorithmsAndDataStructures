#!/bin/python

def insertion_sort(array):
  for i in range(1, len(array)):
    key = array[i]
    j = i - 1

    while j >= 0 and key < array[j] :
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key

nums = [10, 17, 5, 1, 9, 5, 22, 2, 6, 15, 30, 23]

print(nums)
print("After sorting:")
insertion_sort(nums)
print(nums)
