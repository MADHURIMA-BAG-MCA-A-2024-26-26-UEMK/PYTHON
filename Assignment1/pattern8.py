# Number of rows for the top half (including the middle row)
rows = 4

# Top half of the diamond (including the middle row)
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Bottom half of the diamond (excluding the middle row)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)
