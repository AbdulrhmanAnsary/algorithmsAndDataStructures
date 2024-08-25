#!/bin/python

# Find the index of the element by binary search
def find_index(list, value):
  low = 0
  heigh = len(list)

  for _ in range(len(list)):
    try:
      middle = (low + heigh) // 2
      if list[middle] == value:
        return middle
      elif list[middle] > value:
        heigh = middle - 1
      elif list[middle] < value:
        low = middle + 1
      else:
        raise IndexError
    except IndexError as IE:
      print("IndexError:", IE)
      return

nums = list(range(1, 11))
print(find_index(nums, 7))
