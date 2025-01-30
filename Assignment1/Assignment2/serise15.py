# Find the nth term 1,8,54,384,…………………………..
def nth_term(n):
    term = 1  # The first term is 1
    for i in range(1, n):
        term *= (i + 7)  # The factor seems to increase by a small constant each time
    return term

# Example usage:
n = 5  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
