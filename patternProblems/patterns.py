# rows = 5
# columns = 5

# # Rectangular Star Pattern
# for i in range(0, columns):
#   for j in range(0, rows):
#     print('*', end = "")
#   print()


# # Right-Angled Triangle Pattern
# for i in range(columns):
#   for j in range(i+1):
#     print("*", end="")
#   print()


# # Right-Angled Number Pyramid
# for i in range(1, columns + 1):
#   for j in range(1, i + 1):
#     print(j, end= "")
#   print()


# # Right-Angled Number Pyramid - II
# for i in range(1, columns + 1):
#   for j in range(1, i + 1):
#     print(i, end= "")
#   print()


# # Inverted Right Pyramid
# for i in range(columns, 0, -1):
#   for j in range(i):
#     print("*", end="")
#   print()

# # Inverted Numbered Right Pyramid
# for i in range(columns, 0, -1):
#   for j in range(1, i+1):
#     print(j, end="")
#   print()

# # Star Pyramid
# n = 5
# for i in range(1, n + 1):
#   for j in range(1, 2 * n):
#     if (j <= n - i) or (j >= n + i):
#       print(' ', end="")
#     else:
#       print('*', end="")
#   print()

# # Reverse star pattern
# for i in range(n, 0, -1):
#   for j in range(1, 2 * n):
#     if (j <= n - i) or (j >= n + i):
#       print(' ', end="")
#     else:
#       print('*', end="")
#   print()

# # Diamond Star Pattern
# def diamond_star_pattern(n):
#   for i in range(1, n):
#     for j in range(1, 2 * n):
#       if j <= n - i or j >= n + i:
#        print(' ', end="")
#       else:
#        print('*', end="")
#     print()

#   for i in range(n, 0, -1):
#     for j in range(1, 2 * n):
#       if j <= n - i or j >= n + i:
#         print(' ', end="")
#       else:
#         print('*', end="")
#     print()

# diamond_star_pattern(n)

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