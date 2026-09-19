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

def rotate_arr_right(arr, steps):
  steps = steps % len(arr)
  temp_arr = arr[0: len(arr) - steps]

  for i in range(steps):
    arr[i] = arr[len(arr) - steps + i]

  for i in range(steps, len(arr)):
    arr[i] = temp_arr[i - steps]

  return arr

def rotate_arr_left(arr, steps):
  steps = steps % len(arr)

  temp_arr = arr[0: steps]
  for i in range(steps, len(arr)):
    arr[i - steps] = arr[i]

  for i in range(steps):
    arr[len(arr) - steps + i] = temp_arr[i]

  return arr


# print(rotate_arr_left(arr.copy(), 4))

def rotate_arr_left_better(arr, steps):
  steps = steps % len(arr)
  arr_length = len(arr)

  for i in range(arr_length // 2):
    arr[i], arr[arr_length - i - 1] = arr[arr_length - i - 1], arr[i]

  for i in range((arr_length - steps) // 2):
    arr[i], arr[arr_length - steps - i - 1] = arr[arr_length - steps - i - 1], arr[i]

  for i in range(steps // 2):
    left = (arr_length - steps) + i
    right = arr_length - 1 - i
    arr[left], arr[right] = arr[right], arr[left]

  return arr

def rotate_arr_right_better(arr, steps):
  steps = steps % len(arr)
  arr_length = len(arr)

  for i in range(arr_length // 2):
    arr[i], arr[arr_length - i - 1] = arr[arr_length - i - 1], arr[i]

  for i in range((steps) // 2):
    arr[i], arr[steps - i - 1] = arr[steps - i - 1], arr[i]

  for i in range((len(arr) - steps) // 2):
    left = steps + i
    right = arr_length - 1 - i
    arr[left], arr[right] = arr[right], arr[left]

  return arr

# print(rotate_arr_right_better(arr, 2))


def move_zeros_to_end(arr):
  i = 0
  j = 1

  while j < len(arr):
    if arr[i] == 0 and arr[j] != 0:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j += 1
    elif arr[i] == 0 and arr[j] == 0:
      j += 1
    else:
      j += 1
      i += 1

  return arr


# print(move_zeros_to_end([1, 2, 0, 0, 0, 0, 3, 4, 0, 5]))

def find_index(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      return i

  return -1

# print(find_index(arr, 8))
    
def union(arr_1, arr_2):
  union_arr = []
  ptr_1, ptr_2 = 0, 0

  while ptr_1 < len(arr_1) and ptr_2 < len(arr_2):
    if arr_1[ptr_1] == arr_2[ptr_2]:
      if arr_1[ptr_1] not in union_arr:
        union_arr.append(arr_1[ptr_1])
      ptr_1 += 1
      ptr_2 += 1

    elif arr_1[ptr_1] < arr_2[ptr_2]:
      if arr_1[ptr_1] not in union_arr:
        union_arr.append(arr_1[ptr_1])
      ptr_1 += 1

    else:
      if arr_2[ptr_2] not in union_arr:
        union_arr.append(arr_2[ptr_2])
      ptr_2 += 1

  while ptr_1 < len(arr_1):
    if arr_1[ptr_1] not in union_arr:
      union_arr.append(arr_1[ptr_1])
    ptr_1 += 1

  while ptr_2 < len(arr_2):
    if arr_2[ptr_2] not in union_arr:
      union_arr.append(arr_2[ptr_2])
    ptr_2 += 1

  return union_arr

# print(union([1, 2, 2, 2, 2, 3, 4], [0, 0, 0, 0, 1, 2, 3, 8, 9]))

def find_missing_val_from_factorial(arr):
  total_nums = len(arr) + 1
  total_sum = (total_nums * (total_nums + 1)) / 2 

  arr_sum = 0
  for i in range(len(arr)):
    arr_sum += arr[i]

  return total_sum - arr_sum

# print(find_missing_val_from_factorial([1, 2, 4, 5, 6, 7, 8]))

def count_max_consecutive_ones(arr):
  max_count = 0
  count = 0

  i = 0
  for j in range(len(arr)):
    if arr[i] == arr[j] == 1:
      count += 1
    else:
      max_count = max(max_count, count)
      i = j + 1
      count = 0

  return max(max_count, count)

# print(count_max_consecutive_ones([1, 1, 1, 2, 2, 3, 1, 1, 1, 4, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]))

def find_the_lonely_no(arr):
  max_val = arr[0]
  for i in arr:
    if i > max_val:
      max_val = i

  hash_arr = [0] * max_val
  for i in arr:
    hash_arr[i - 1] += 1

  for i in range(len(hash_arr)):
    if hash_arr[i] == 1:
      return i + 1

# print(find_the_lonely_no([1, 2, 3, 3, 1, 4, 2, 4, 7]))


def longest_sub_array_length_brute(arr, k):
  max_len = 0
  for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
      sum += arr[j]

      if sum == k:
        max_len = max(max_len, j - i + 1)

  return max_len

def longest_sub_array_length_better(arr, k):
  max_len = 0
  pre_sum_map = {}
  arr_sum = 0

  for i in range(len(arr)):
    arr_sum += arr[i]

    if arr_sum == k:
      max_len = i + 1

    rem = arr_sum - k
    if rem in pre_sum_map:
      length = i - pre_sum_map[rem]
      max_len = max(max_len, length)

    if arr_sum not in pre_sum_map:
      pre_sum_map[arr_sum] = i

  return max_len





print(longest_sub_array_length_better([1, -1, 5, -2, 3], 3))
