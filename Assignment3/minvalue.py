# 6.Given a sorted array of positive integers arr, and an integer n which represents the length of arr, the task is to rearrange the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

def rearrange_array(arr, n):
    # Create a new result array to store the rearranged elements
    result = [0] * n
    
    # Two pointers: one at the beginning (left) and one at the end (right)
    left = 0
    right = n - 1
    
    # Iterate over the result array
    for i in range(n):
        if i % 2 == 0:  # Even index - pick the maximum element
            result[i] = arr[right]
            right -= 1
        else:  # Odd index - pick the minimum element
            result[i] = arr[left]
            left += 1
    
    # Print the rearranged array
    print("Rearranged array:", result)

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
rearrange_array(arr, n)
