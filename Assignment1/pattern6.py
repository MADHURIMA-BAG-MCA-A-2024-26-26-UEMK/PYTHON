# Number of rows
rows = 4

# Loop to print the pattern
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)
