#  Find the nth term 1,1,2,6,24,………………………………
import math

def nth_term(n):
    return math.factorial(n)

# Example usage:
n = 5  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
