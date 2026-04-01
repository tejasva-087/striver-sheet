import math

# ****************************
# Count digits in a number
# ****************************
def count_num_digits(num):
  return math.floor(math.log10(num)) + 1

# print(count_num_digits(12345))
# print(count_num_digits(1234))


# ****************************
# Reverse Digits of A Number
# ****************************
def reverse_number(num):
  reverse_num = 0
  

  while num > 0:
    last_digit = num % 10
    reverse_num = reverse_num * 10 + last_digit
    num = num // 10

  return reverse_num


# print(reverse_number(123))
# print(reverse_number(1234))

 
# ****************************************
# Check if a number is Palindrome or Not
# ****************************************

def check_palindrome(num):
  reversed_num = reverse_number(num)
  return reversed_num == num

# print(check_palindrome(1001))
# print(check_palindrome(10011))

# ****************************************
# GCD brute force
# ****************************************
def gcd(num_1, num_2):
  minimum = num_1 if num_1 < num_2 else num_2
  for i in range(minimum, 0, -1):
    if (num_1 % i == 0) and (num_2 % i == 0):
      return i
  return None

# print(gcd(20, 15))
# print(gcd(11, 7))
# print(gcd(24, 6))

# ****************************************
# GCD euclidean algorithm
# ****************************************
def gcd_euclidean_algorithm(num_1, num_2):
  while num_1 > 0 and num_2 > 0:
    if num_1 > num_2:
      num_1 -= num_2
    else:
      num_2 -= num_1
  return num_2 if num_1 == 0 else num_1


# print(gcd_euclidean_algorithm(20, 15))
# print(gcd_euclidean_algorithm(11, 7))
# print(gcd_euclidean_algorithm(24, 6))


# ****************************************
# Check if a number is Armstrong or Not
# ****************************************
def check_armstrong(num):
  if num == 0:
    return True
  
  total = 0
  n = num
  num_digits = count_num_digits(num)

  while n > 0:
    total += (n % 10) ** num_digits
    n //= 10
  
  return num == total


# print(check_armstrong(371))
# print(check_armstrong(31))


# ****************************************************
# Print all Divisors of a given Number (brute force)
# ****************************************************
def find_divisor(num):
  divisor = []
  for i in range(1, num + 1):
    if num % i == 0:
      divisor.append(i)
  return divisor

# print(find_divisor(12))
# print(find_divisor(4))

# ********************************************************
# Print all Divisors of a given Number (optimal approach)
# ********************************************************
def find_divisor_optimal(n):
  divisor = set()
  for i in range(1, math.floor(n ** 0.5) + 1):
    if n % i == 0:
      divisor.add(i)
      divisor.add(int(n / i))
  return list(divisor)

# print(find_divisor_optimal(12))
# print(find_divisor_optimal(4))

# ********************************************************
# Check for prime numbers
# ********************************************************
def check_prime(n):
  if n == 0 or n == 1:
    return False
  
  if n == 2:
    return True
  
  for i in range(3, n + 1):
    if n % i == 0 and i != n:
      return False
  
  return True

print(check_prime(27))