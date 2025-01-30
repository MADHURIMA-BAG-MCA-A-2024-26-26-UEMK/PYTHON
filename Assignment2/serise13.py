# Find the nth term 14,28,20,40,…………………………….
def nth_term(n):
    if n % 2 == 1:
        # Odd-index terms (1st, 3rd, 5th, ...) increase by 6 each time
        return 14 + (n // 2) * 6
    else:
        # Even-index terms (2nd, 4th, 6th, ...) double the previous term
        return 28 * (2 ** ((n // 2) - 1))

# Example usage:
n = 5  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
