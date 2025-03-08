def generate_subsets(arr, current=[], index=0):
    # Base case: If we've gone through all elements, print the current subset
    if index == len(arr):
        print(current)
        return
    # Recursive case 1: Exclude the current element and move to the next
    generate_subsets(arr, current, index + 1)
    # Recursive case 2: Include the current element and move to the next
    generate_subsets(arr, current + [arr[index]], index + 1)

# Calling the function with a sample set
generate_subsets([1, 2, 3])
