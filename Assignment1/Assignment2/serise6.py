# 1*2*3+2*3*4+……………………………….+n*(n+1)*(n+2)
def series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i * (i + 1) * (i + 2)
    return total

# Example usage:
n = 5  # You can change n to any integer
result = series_sum(n)
print(f"The sum of the series is: {result}")
