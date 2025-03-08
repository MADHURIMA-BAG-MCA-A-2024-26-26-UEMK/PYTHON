def split_tuple(t):
    # Find the midpoint of the tuple
    midpoint = len(t) // 2
    # Print the first half and the last half of the tuple
    print("First half:", t[:midpoint])
    print("Last half:", t[midpoint:])

# Calling the function with the given tuple
split_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
