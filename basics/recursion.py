def print_n_times(n, string):
  if n == 0:
    return
  print(string)
  print_n_times(n - 1, string)

# print_n_times(5, 'name')

def print_1_to_n(n, i=1):
  print(i)

  if (n == 1):
    return
  
  print_1_to_n(n-1, i+1)

# print_1_to_n(5)

def print_n_to_1(n):
  print(n)

  if (n == 1):
    return
  
  print_n_to_1(n-1)

# print_n_to_1(5)

def sum_n_num(n):
  if (n == 1):
    return 1

  return n + sum_n_num(n-1)

# print(sum_n_num(5))

def factorial(n):
  if (n == 1):
    return 1

  return n * factorial(n-1)

# print(factorial(3))


# brute force
def reverse_arr_brute(arr):
  rev_arr = []

  def helper_func(arr, n):
    if (n == 0):
      return
    
    rev_arr.append(arr[n-1])
    return helper_func(arr, n - 1)

  helper_func(arr, len(arr))

  return rev_arr

# two pointer better
def reverse_arr(arr, ptr_1, ptr_2):
  if (ptr_2 <= ptr_1):
    return arr

  arr[ptr_2], arr[ptr_1] = arr[ptr_1], arr[ptr_2]
  return reverse_arr(arr, ptr_1 + 1, ptr_2 - 1)

# print(reverse_arr([1, 2, 3, 4, 5, 6], 0, 5))

def is_palindrome(string):

  def helper(string, ptr_1, ptr_2):
    print(string, string[ptr_1], string[ptr_2])
    if string[ptr_1] != string[ptr_2]:
          return False
    
    if (ptr_2 <= ptr_1):
      return True

    return helper(string, ptr_1 + 1, ptr_2 - 1)

  return helper(string, 0, len(string) - 1)

# print(is_palindrome('abcddacba'))

def fibonacci(i):
  if i == 0:
    return
  
  def helper(i, n1, n2):
    print(n1)
    if (i == 1):
      return
  
    return helper(i - 1, n2, n1 + n2)

  helper(i, 0, 1)


# fibonacci(10)