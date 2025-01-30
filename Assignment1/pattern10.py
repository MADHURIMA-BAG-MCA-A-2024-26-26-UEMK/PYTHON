# Number of rows and columns (square size)
size = 4

# Loop to print each row
for i in range(size):
    if i == 0 or i == size - 1:
        # Print the first and last rows with stars
        print("* " * size)
    else:
        # Print the middle rows with stars at the edges and spaces in between
        print("*", " " * (2 * (size - 2)), "*")
