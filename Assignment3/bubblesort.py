# 9.Write a program to input a list of numbers and sort using bubble sort.

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize if the list is already sorted
        swapped = False
        
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break

# Input: A list of numbers
arr = list(map(int, input("Enter the list of numbers separated by space: ").split()))

# Call bubble_sort function
bubble_sort(arr)

# Output the sorted list
print("Sorted list:", arr)
