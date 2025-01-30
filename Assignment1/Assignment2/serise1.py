# 11+2!+3!+…………….+n! 
import math

def factorial_sum(n):
    total_sum = 11  # Starting with 11
    for i in range(2, n + 1):
        total_sum += math.factorial(i)  # Add factorial of i to the sum
    return total_sum

# Get user input for the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum
result = factorial_sum(n)

# Output the result
print(f"The sum of the series 11 + 2! + 3! + ... + {n}! is: {result}")
