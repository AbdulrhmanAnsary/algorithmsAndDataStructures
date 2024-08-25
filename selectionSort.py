#!/bin/python

def selection_sort(list):
  for i in range(len(list)):
    min_index = i
    for j in range(i, len(list)):
      if list[j] < list[min_index]:
        min_index = j
    list[min_index], list[i] = list[i], list[min_index]
  return list

nums = [10, 17, 5, 1, 90, 23, 110, 237, 90, 926, 973, 19, 375]

print(nums)
print("After sorting:")
print(selection_sort(nums))
