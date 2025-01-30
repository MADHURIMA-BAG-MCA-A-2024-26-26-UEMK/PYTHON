# 10.Write a program to input a list of numbers and sort using insertion sort.

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move the element to the right
            j -= 1
        
        # Insert the key in its correct position
        arr[j + 1] = key

# Input: A list of numbers
arr = list(map(int, input("Enter the list of numbers separated by space: ").split()))

# Call insertion_sort function
insertion_sort(arr)

# Output the sorted list
print("Sorted list:", arr)
