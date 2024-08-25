#!/usr/bin/python

def merge_two_sorted_arrays(array1, array2):
  result = []
  i = j = 0

  while i != len(array1) or j != len(array2):
    if i < len(array1) and j >= len(array2):
      result.append(array1[i])
      i += 1
    elif i >= len(array1) and j < len(array2):
      result.append(array2[j])
      j += 1
    else:
      if array1[i] <= array2[j]:
        result.append(array1[i])
        i += 1
      elif array1[i] >= array2[j]:
        result.append(array2[j])
        j += 1
  return result

def merge_sort(array):
  if len(array) <= 1:
    return array
  middle = len(array) // 2
  array1 = merge_sort(array[0:middle])
  array2 = merge_sort(array[middle:])

  return merge_two_sorted_arrays(array1, array2)

nums = [17, 10, 5, 1, 9, 7, 2, 1, 5, 17, 22, 8]

print(nums)
print("After sorting:")
print(merge_sort(nums))
