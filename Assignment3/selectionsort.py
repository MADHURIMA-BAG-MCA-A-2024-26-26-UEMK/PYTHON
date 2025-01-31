# Write a program to input a list of numbers and sort using selection sort.

# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input the list of numbers
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Perform selection sort
selection_sort(numbers)

# Output the sorted list
print("Sorted list:", numbers)
