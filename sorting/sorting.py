def selection_sort(arr):
  for i in range(len(arr)):
    shortest_val_position = 0

    for j in range(1, len(arr)):
      if arr[j] < arr[i]:
        shortest_val_position = j

    arr[i], arr[shortest_val_position] = arr[shortest_val_position], arr[i]

  return arr

# print(selection_sort([3, 4, 1, 2, 10]))

def bubble_sort(arr):
  for i in range(len(arr), 0, -1):
    for j in range(0, i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        
  return arr

# print(bubble_sort([3, 4, 2, 1, 1]))

def insertion_sort(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]

      for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
          arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
          break

  return arr

# print(insertion_sort([3, 5, 9, 1, 1, 0, 1]))

def merge_sort(arr, left_ptr, right_ptr):
  if left_ptr >= right_ptr:
    return

  mid_ptr = (right_ptr + left_ptr) // 2

  merge_sort(arr, left_ptr, mid_ptr)
  merge_sort(arr, mid_ptr + 1, right_ptr)

  left_arr = arr[left_ptr: mid_ptr + 1]
  right_arr = arr[mid_ptr + 1: right_ptr + 1]
  left_arr_ptr = 0
  right_arr_ptr = 0

  sorted_arr = []

  while left_arr_ptr < len(left_arr) and right_arr_ptr < len(right_arr):
    if left_arr[left_arr_ptr] < right_arr[right_arr_ptr]:
      sorted_arr.append(left_arr[left_arr_ptr])
      left_arr_ptr += 1
    else:
      sorted_arr.append(right_arr[right_arr_ptr])
      right_arr_ptr += 1

  for i in range(left_arr_ptr, len(left_arr)):
    sorted_arr.append(left_arr[i])

  for i in range(right_arr_ptr, len(right_arr)):
    sorted_arr.append(right_arr[i])

  for i in range(len(sorted_arr)):
    arr[left_ptr + i] = sorted_arr[i]

  return arr

# print(merge_sort([2, 3, 1, 4, 1], 0, 4))

def recursive_bubble_sort(arr, end=None):
  if end == None:
    end = len(arr)

  if end <= 1:
    return arr
  
  for i in range(end - 1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]

  return recursive_bubble_sort(arr, end - 1)

# print(recursive_bubble_sort([3, 2, 2, 4, 9, 8]))

def recursive_insertion_sort(arr, i=0):
  if i >= len(arr) - 2:
    return arr
  
  for j in range(i + 1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
      break
        
  return recursive_bubble_sort(arr, i+1)

# print(bubble_sort([2, 3, 1, 4, 5, 0]))

def quick_sort(arr, start=0, end=None):
  if end == None:
    end = len(arr)

  if start >= end:
    return arr

  pivot_index = (start + end - 1) // 2
  pivot_value = arr[pivot_index]
  arr[pivot_index], arr[end - 1] = arr[end - 1], arr[pivot_index]

  position = start
  for k in range(start, end - 1):
    if arr[k] < pivot_value:
      arr[k], arr[position] = arr[position], arr[k]
      position += 1
  arr[position], arr[end - 1] = arr[end - 1], arr[position]


  quick_sort(arr, start, position)
  quick_sort(arr, position + 1, end)
  return arr


print(quick_sort([3, 4, 2, 1, 1, 1, 0, 9, 12, 0]))
