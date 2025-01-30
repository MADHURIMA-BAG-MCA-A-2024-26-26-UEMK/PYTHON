# Find the nth term 0,0,2,1,4,2,6,3,8………………………
def nth_term(n):
    if n % 2 == 1:
        # Odd-index terms: (0, 2, 4, 6, 8, ...)
        return 2 * (n // 2)
    else:
        # Even-index terms: (0, 1, 2, 3, ...)
        return n // 2 - 1

# Example usage:
n = 9  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
