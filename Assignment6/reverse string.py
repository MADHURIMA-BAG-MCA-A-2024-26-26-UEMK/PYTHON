def reverse_string(s):
    if len(s) == 0:
        return s
    # Swap the first and last character and recurse
    return reverse_string(s[1:]) + s[0]

# Calling the function with a sample string
reversed_str = reverse_string("hello")
print(reversed_str)
