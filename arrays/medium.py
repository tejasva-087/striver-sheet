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


print(two_sum([1, 4, 8, 9, 5, 2, 4], 8))
  