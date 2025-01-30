# 1+x+x^2+x^3+……………………………………+x^n
def series_sum(x, n):
    total = 0
    for i in range(n + 1):
        total += x**i
    return total

# Example usage:
x = 2  # You can change x to any value
n = 5  # You can change n to any integer
result = series_sum(x, n)
print(f"The sum of the series is: {result}")
