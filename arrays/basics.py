arr = [1, 2, 3, 4, 5, 6, 7]

def highest_element(arr):
  highest = arr[0]
  for i in arr:
    if i > highest:
      highest = i

  return highest

# print(highest_element([2, 3, 1, 5, 8, 9, 12, 1, 0]))

def second_largest_and_smallest(arr):
  highest = arr[0]
  lowest = arr[0]

  second_highest = arr[0]
  second_lowest = arr[0]

  for i in arr:
    if i > highest:
      highest = i
    elif i < lowest:
      lowest = i

  for i in arr:
    if i > second_highest and i != highest:
      second_highest = i
    elif i < second_lowest and i != lowest:
      second_lowest = i

  return [second_highest, second_lowest]


# print(second_largest_and_smallest(arr))

def check_sorted(arr):
  for i in range(len(arr) - 1):
    if not arr[i] <= arr[i + 1]:
      return False

  return True

# print(check_sorted(arr))

def remove_duplicate(arr):
  new_arr = []

  ptr = 0
  for i in range(1, len(arr)):
    if arr[ptr] != arr[i]:
      new_arr.append(arr[ptr])
      ptr = i
  new_arr.append(arr[ptr])

  return new_arr

# print(remove_duplicate(arr))

def rotate_left(arr):
  new_arr = arr.copy()
  for i in range(1, len(arr)):
    arr[i], arr[i - 1] = arr[i - 1], arr[i]

  return new_arr



# print(rotate_left(arr))

def rotate_arr(arr, num = 1, direction = 'left'):
  rotated_arr = []

  if direction == 'left':
    elements = arr[0: num]

    for i in range(num, len(arr)):
      rotated_arr.append(arr[i])

    for i in elements:
      rotated_arr.append(i)
    
  else:
    elements = arr[len(arr) - num: len(arr)]

    for i in range(len(elements)-1, -1, -1):
      rotated_arr.append(elements[i])

    for i in range(0, num):
      rotated_arr.append(arr[i])

  return rotated_arr

print(rotate_arr(arr, 3, 'right'))