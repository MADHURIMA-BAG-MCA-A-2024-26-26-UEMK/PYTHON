# 1/1^1+2/2^2+3/3^3+………………….+n/n^n
def series_sum(n):
    total_sum = 0  # Start with sum 0
    for i in range(1, n + 1):
        total_sum += i / (i ** i)  # Add i / i^i to the sum
    return total_sum

# Get user input for the value of n
n = int(input("Enter the value of n: "))

# Calculate the sum
result = series_sum(n)

# Output the result
print(f"The sum of the series 1/1^1 + 2/2^2 + 3/3^3 + ... + {n}/{n}^{n} is: {result}")
