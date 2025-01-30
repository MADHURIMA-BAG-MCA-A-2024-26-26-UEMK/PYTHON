# Write a program that prints a list where the values are square of numbers between 5000 and 7000 (both included).

def square_numbers_in_range():
    # List to store squares of numbers between 5000 and 7000
    squares = []
    
    # Loop through the numbers from 5000 to 7000 (both inclusive)
    for num in range(5000, 7001):
        squares.append(num ** 2)  # Append the square of the number to the list
    
    # Print the list of squares
    print("List of squares of numbers between 5000 and 7000:")
    print(squares)

# Call the function
square_numbers_in_range()
