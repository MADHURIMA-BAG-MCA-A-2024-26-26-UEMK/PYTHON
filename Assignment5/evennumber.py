# Function to print even numbers from a list
def print_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Accepting input list from the user
input_list = [int(x) for x in input("Enter a list of numbers (separated by space): ").split()]

# Calling the function and getting the result
even_numbers = print_even_numbers(input_list)

# Printing the result
print(f"The even numbers from the list are: {even_numbers}")
