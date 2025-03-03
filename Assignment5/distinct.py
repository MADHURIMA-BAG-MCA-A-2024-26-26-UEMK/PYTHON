# Function to return a new list with distinct elements
def distinct_elements(input_list):
    # Using set to remove duplicates, then converting it back to a list
    return list(set(input_list))

# Accepting input list from the user
input_list = [int(x) for x in input("Enter a list of numbers (separated by space): ").split()]

# Calling the function and getting the result
distinct_list = distinct_elements(input_list)

# Printing the result
print(f"The list with distinct elements is: {distinct_list}")
