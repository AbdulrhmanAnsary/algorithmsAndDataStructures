#!/usr/bin/env python

def merge_two_sorted_arrays(array1, array2):
  result = []
  i = j = 0

  while i < len(array1) or j < len(array2):
    if i < len(array1) and (j >= len(array2) or array1[i] <= array2[j]):
      result.append(array1[i])
      i += 1
    else:
      result.append(array2[j])
      j += 1
  return result

def merge_sort(array):
  if len(array) <= 1:
    return array
  middle = len(array) // 2
  left_half = merge_sort(array[:middle])
  right_half = merge_sort(array[middle:])

  return merge_two_sorted_arrays(left_half, right_half)

nums = [5, 6, 9, 10, 22, 77, 1, 2, 5, 5, 7, 8, 9, 3]

print("Original array:")
print(nums)
print("After merge sort:")
print(merge_sort(nums))
