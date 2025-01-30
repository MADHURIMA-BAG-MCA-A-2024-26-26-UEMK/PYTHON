#Find the nth term 2,4,3,4,15,…………………………
def nth_term(n):
    # We can make the odd terms follow one pattern and even terms follow another.
    if n % 2 == 1:
        # Odd-index terms: following a simple alternating pattern
        if n == 1:
            return 2
        else:
            return n // 2 + 2  # Alternating increment pattern
    else:
        # Even-index terms: larger jumps for these
        return n ** 2 - n  # A hypothetical rule for jumps (may need adjustment)

# Example usage:
n = 6  # You can change n to get the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
