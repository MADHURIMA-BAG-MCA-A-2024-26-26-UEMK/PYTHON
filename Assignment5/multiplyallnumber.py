# Function to multiply all numbers in a list
def multiply_of_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# Calling the function and printing the result
product = multiply_of_list(numbers)
print(f"The product of all the numbers in the list is: {product}")
