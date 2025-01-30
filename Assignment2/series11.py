# Find the nth term 3,5,33,35,53,……………………..
def nth_term(n):
    if n % 2 == 1:
        # Odd terms: Start with 3 and keep adding 2 (3, 33, 53, ...)
        return 3 + (n // 2) * 20
    else:
        # Even terms: Start with 5 and add alternating larger numbers
        return 5 + (n // 2 - 1) * 28

# Example usage:
n = 6  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
