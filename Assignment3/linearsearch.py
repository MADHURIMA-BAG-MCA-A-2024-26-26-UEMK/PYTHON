# 7.Write a program to input a number and search in a list using linear search.

def linear_search(arr, target):
    # Loop through each element in the list
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Input: A list of numbers
arr = list(map(int, input("Enter the list of numbers separated by space: ").split()))

# Input: The number to search
target = int(input("Enter the number to search: "))

# Perform linear search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found in the list.")
