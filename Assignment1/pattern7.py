# Number of rows
rows = 4

# Function to generate Pascal's Triangle
def generate_pascals_triangle(rows):
    triangle = []
    
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle

# Function to print the triangle in the specified format
def print_pascals_triangle(triangle):
    for i in range(len(triangle)):
        print(" " * (len(triangle) - i - 1), end="")  # Add leading spaces
        print(" ".join(map(str, triangle[i])))  # Print the numbers in the row

# Generate and print the Pascal's Triangle
triangle = generate_pascals_triangle(rows)
print_pascals_triangle(triangle)
