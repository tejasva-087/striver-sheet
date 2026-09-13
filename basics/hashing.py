def count_frequency(arr):
  frequency_map = {}

  for i in arr:
    if i in frequency_map.keys():
      frequency_map[i] += 1
    else:
      frequency_map[i] = 1

  return frequency_map

# print(count_frequency([1, 3, 3, 3, 2, 1]))

def highest_and_lowest(arr):
  frequency = count_frequency(arr)

  lowest_freq = float('inf')
  highest_freq = 0
  lowest_element = 0
  highest_element = 0

  for i in frequency:
    if frequency[i] > highest_freq:
      highest_freq = frequency[i]
      highest_element = i
    elif frequency[i] < lowest_freq:
      lowest_freq = frequency[i]
      lowest_element = i
  
  return [lowest_element, highest_element]

# print(highest_and_lowest([1, 2, 2, 3, 1, 1, 1]))