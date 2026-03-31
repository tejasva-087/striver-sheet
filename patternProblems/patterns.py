rows = 5
columns = 5

# Rectangular Star Pattern
for i in range(0, columns):
  for j in range(0, rows):
    print('*', end = "")
  print()


# Right-Angled Triangle Pattern
for i in range(columns):
  for j in range(i+1):
    print("*", end="")
  print()


# Right-Angled Number Pyramid
for i in range(1, columns + 1):
  for j in range(1, i + 1):
    print(j, end= "")
  print()


# Right-Angled Number Pyramid - II
for i in range(1, columns + 1):
  for j in range(1, i + 1):
    print(i, end= "")
  print()


# Inverted Right Pyramid
for i in range(columns, 0, -1):
  for j in range(i):
    print("*", end="")
  print()

# Inverted Numbered Right Pyramid
for i in range(columns, 0, -1):
  for j in range(1, i+1):
    print(j, end="")
  print()

# Star Pyramid
n = 5
for i in range(1, n + 1):
  for j in range(1, 2 * n):
    if (j <= n - i) or (j >= n + i):
      print(' ', end="")
    else:
      print('*', end="")
  print()

# Reverse star pattern
for i in range(n, 0, -1):
  for j in range(1, 2 * n):
    if (j <= n - i) or (j >= n + i):
      print(' ', end="")
    else:
      print('*', end="")
  print()

# Diamond Star Pattern
def diamond_star_pattern(n):
  for i in range(1, n):
    for j in range(1, 2 * n):
      if j <= n - i or j >= n + i:
       print(' ', end="")
      else:
       print('*', end="")
    print()

  for i in range(n, 0, -1):
    for j in range(1, 2 * n):
      if j <= n - i or j >= n + i:
        print(' ', end="")
      else:
        print('*', end="")
    print()

diamond_star_pattern(n)

# Half Diamond Star Pattern
def half_diamond(n):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if j <= i:
        print('*', end="")
      else:
        print(' ', end="")
    print()

  for i in range(n, 0, -1):
    for j in range(1, n):
      if i <= j:
        print(' ', end="")
      else:
        print('*', end='')
    print()


half_diamond(3)

# Binary Number Triangle Pattern
  
n = 5
start = 1
for i in range(n):
  if i % 2 == 0:
    start = 1
  else:
    start = 0

  for j in range(i + 1):
    print(start, end='')
    start = 1 - start
  print()


# Number Crown Pattern
n = 5
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if (j <= i):
      print(j, end='')
    else:
      print(0, end='')

  for j in range(n, 0, -1):
    if (j <= i):
      print(j, end='')
    else:
      print(' ', end='')
  print()


# Increasing Number Triangle Pattern
n = 5
start = 1
for i in range(n):
  for j in range(i + 1):
    print(start, end=" ")
    start += 1
  print()

# Increasing Letter Triangle Pattern
n = 5
for i in range(n):
  for j in range(i + 1):
    print(chr(65 + j), end='')
  print()

# Reverse Letter Triangle Pattern
n = 5
for i in range(n, 0, -1):
  for j in range(i):
    print(chr(65 + j), end='')
  print()

# Alpha-Ramp Pattern
n = 5
for i in range(n):
  for j in range(i + 1):
    print(chr(65 + i), end="")
  print()


n = 5
for i in range(n):
  print(' ' * (n - i - 1), end='')

  breakpoint = (2 * i + 1) // 2
  ch = ord('A')

  for j in range(0, 2 * i + 1):
    print(chr(ch), end= '')
    
    if j < breakpoint:
      ch += 1
    else:
      ch -= 1

  print()

# Alpha-Triangle Pattern
n = 5
for i in range(n - 1, -1, -1):
  ch = ord('A') + i
  for j in range(0, n - i):
    print(chr(ch), end='')
    ch += 1
  print()


# Symmetric-Void Pattern
n = 5
for i in range(1, 2 * n + 1):
  if i <= n:
    for j in range(n):
      if j <= n - i:
        print('*', end="")
      else:
        print(" ", end="")
    
    for j in range(n - 1, -1, -1):
      if j <= n - i:
        print('*', end="")
      else:
        print(" ", end="")

  else:
    for j in range(n):
      if j < i - n:
        print("*", end="")
      else:
        print(" ", end="")

    
    for j in range(n - 1, -1, -1):
      if j < i - n:
        print("*", end="")
      else:
        print(" ", end="")

  print()

# Symmetric-Butterfly Pattern
n = 4
for i in range(1, 2 * n):
    if i <= n:
      for j in range(n):
        if j < i:
          print('*', end="")
        else:
          print(' ', end="")
      
      for j in range(n - 1, -1, -1):
        if j < i:
          print('*', end="")
        else:
          print(' ', end="")

    else:
      for j in range(n - 1, -1, -1):
        if j >= i - n:
          print('*', end="")
        else:
          print(' ', end="")
      
      for j in range(n):
        if j >= i - n:
          print('*', end="")
        else:
          print(' ', end="")
    print()

# Hollow Rectangle Pattern
n = 6
for i in range(n):
  if i == 0 or i == n - 1:
    for j in range(n):
      print('*', end="")
  else:
    for j in range(n):
      if j == 0 or j == n - 1:
        print('*', end="")
      else:
        print(' ', end="")
  print()


# The Number Pattern
n = 3
for i in range(1, n + 1):
  for j in range(1, n + 1):
    print(n - min(i, j) + 1, end="")
  for j in range(n - 1, 0, -1):
    print(n - min(i, j) + 1, end="")
  print()

for i in range(n - 1, 0, -1):
  for j in range(1, n + 1):
    print(n - min(i, j) + 1, end="")
  for j in range(n - 1, 0, -1):
    print(n - min(i, j) + 1, end="")
  print()

