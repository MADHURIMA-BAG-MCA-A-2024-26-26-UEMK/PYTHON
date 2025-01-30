# 1*3+3*5+………………………………………………….
def series_sum(m):
    total = 0
    for i in range(1, m + 1):
        total += (2*i - 1) * (2*i + 1)
    return total

# Example usage:
m = 5  # You can change m to the number of terms you want
result = series_sum(m)
print(f"The sum of the series is: {result}")
