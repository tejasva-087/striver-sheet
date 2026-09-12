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