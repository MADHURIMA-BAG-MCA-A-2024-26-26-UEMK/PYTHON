# Number of rows for the pattern
rows = 4

# Top half of the pattern
for i in range(rows):
    print(" " * (2 * (rows - i - 1)) + "*", end="")
    print(" " * (4 * i) + "*")

# Bottom half of the pattern
for i in range(rows - 1):
    print(" " * (2 * (i + 1)) + "*", end="")
    print(" " * (4 * (rows - i - 2)) + "*")
