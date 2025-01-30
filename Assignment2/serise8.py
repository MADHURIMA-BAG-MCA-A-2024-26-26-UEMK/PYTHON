# 1-x^2/2!+x^4/4!+…………………………………………….
import math

def series_sum(x, terms):
    total = 0
    for n in range(terms):
        # Each term is (-1)^n * (x^(2n)) / (2n)!
        total += ((-1)**n * x**(2*n)) / math.factorial(2*n)
    return total

# Example usage:
x = 2  # You can change x to any value
terms = 10  # You can change terms to the number of terms you want to calculate
result = series_sum(x, terms)
print(f"The sum of the series is: {result}")
