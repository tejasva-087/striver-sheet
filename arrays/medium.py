def two_sum(arr, sum):
  arr_map = []

  for i in range(len(arr)):
    arr_map.append([arr[i], i])

  arr_map.sort()

  left = 0
  right = len(arr_map) - 1

  while left < right:
    window_sum = arr_map[left][0] + arr_map[right][0]

    if window_sum == sum:
      return [arr_map[left][1], arr_map[right][1]]
    elif window_sum > sum:
      right -= 1
    else:
      left += 1

  return [-1, -1]


# print(two_sum([1, 4, 8, 9, 5, 2, 4], 8))

# dutch national flag algorithm
# 0's -> 0 to low - 1
# 1's -> low to mid - 1
# 2's -> high + 1 to len(arr) - 1
def dnf_sort(arr):
  low, mid, high = 0, 0, len(arr) - 1

  while mid <= high:
    print(arr, low, mid, high)
    if arr[mid] == 0:
      arr[mid], arr[low] = arr[low], arr[mid]
      low += 1
      mid += 1
    elif arr[mid] == 1:
      mid += 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high -= 1

  return arr

# print(dnf_sort([1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1]))

def find_majority_occurring_num(arr):
  leader = arr[0]
  strength = 1

  for i in range(1, len(arr)):
    if strength == 0:
      leader = arr[i]

    if leader == arr[i]:
      strength += 1
    else:
      strength -= 1

  return leader

# print(find_majority_occurring_num([2, 2, 1, 1, 3, 4, 1, 1, 1, 1, 1]))

def max_subarray_sum(arr):
  current_sum = arr[0]
  max_sum = arr[0]

  temp_start = 0
  start = 0
  end = 0

  for i in range(1, len(arr)):
    if arr[i] > current_sum + arr[i]:
      current_sum = arr[i]
      temp_start = i
    else:
      current_sum += arr[i]

    if max_sum < current_sum:
      max_sum = current_sum
      start = temp_start
      end = i

  return [max_sum, start, end]

# print(max_subarray_sum([-21, -8, -5, -4, -9]))

def buy_sell_stock(arr):
  min_buy_val = arr[0]
  profit = 0

  buy_day = 0
  sell_day = 0
  temp_buy_day = 0

  for i in range(1, len(arr)):
    sell_val = arr[i] - min_buy_val

    if sell_val > profit:
      profit = sell_val
      sell_day = i
      buy_day = temp_buy_day

    if arr[i] < min_buy_val:
      min_buy_val = arr[i]
      temp_buy_day = i

  return [buy_day + 1, sell_day + 1, profit]

print(buy_sell_stock([5, 3, 6, 1]))
