#!/usr/bin/env python

def mergeSort(array):
  if len(array) > 1:
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    mergeSort(left_half)
    mergeSort(right_half)
    merge(array, left_half, right_half)

def merge(container, first_array, second_array):
  i = j = k = 0

  # Add the two arrays in the container
  while i < len(first_array) and j < len(second_array):
    if first_array[i] < second_array[j]:
      container[k] = first_array[i]
      i += 1
    else:
      container[k] = second_array[j]
      j += 1
    k += 1

  # Add the remains from the first array
  while i < len(first_array):
    container[k] = first_array[i]
    i += 1
    k += 1

  # Add the remains from the second array
  while j < len(second_array):
    container[k] = second_array[j]
    j += 1
    k += 1

nums = [3, 7, 1, 5, 6, 7, 9, 2]

print(nums)
mergeSort(nums)
print("After merge sort:")
print(nums)
