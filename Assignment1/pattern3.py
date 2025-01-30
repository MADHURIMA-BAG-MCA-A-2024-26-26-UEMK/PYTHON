# Number of rows
rows = 5

# Starting number
num = 1

# Loop to print the pattern
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()  # Move to the next line after each row
