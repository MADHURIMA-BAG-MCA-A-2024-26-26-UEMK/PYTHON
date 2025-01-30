# 8.Write a program to input a number and search in a list using binary search.

def binary_search(arr, target):
    # Initializing the left and right pointers
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index if found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Return -1 if the target is not found

# Input: A sorted list of numbers
arr = list(map(int, input("Enter the sorted list of numbers separated by space: ").split()))

# Input: The number to search
target = int(input("Enter the number to search: "))

# Perform binary search
result = binary_search(arr, target)

# Output the result
if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found in the list.")
