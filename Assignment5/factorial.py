# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Taking input from the user
number = int(input("Enter a number to find its factorial: "))

# Calling the function and printing the result
result = factorial(number)
print(f"The factorial of {number} is: {result}")
