def max_string_length(str1, str2):
    # Compare the lengths of the two strings
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        # If the lengths are the same, print both strings line by line
        print(str1)
        print(str2)

# Calling the function with two strings of different lengths
max_string_length("apple", "banana")

# Calling the function with two strings of the same length
max_string_length("hello", "world")
