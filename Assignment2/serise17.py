# Find the nth term 0,6,0,12,0,90,……………………
def nth_term(n):
    if n % 2 == 1:
        # Odd-index terms (1st, 3rd, 5th, ...) are 0
        return 0
    else:
        # Even-index terms: Follow a pattern we observed
        factor = 2 ** (n // 2)  # This could be an approximation for now
        return factor * (n // 2)  # Multiply by the term number

# Example usage:
n = 6  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
