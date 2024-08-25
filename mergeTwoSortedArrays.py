#!/bin/python

def merge_arrays(array1, array2):
  result = []
  i = 0
  j = 0

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

array1 = [5, 2, 7, 8, 5, 2, 4, 1, 9, 3]
array2 = [3, 9, 5, 10, 22, 77, 6]

print("Array1:")
print(array1)
print("Array2:")
print(array2)
print("After merge:")
print(merge_arrays(array1, array2))
