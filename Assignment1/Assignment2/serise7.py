# 1-1/2+1/3-1/4+………………………………………………..
def alternating_series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += (-1)**(i + 1) * (1 / i)
    return total

# Example usage:
n = 10  # You can change n to the number of terms you want
result = alternating_series_sum(n)
print(f"The sum of the series is: {result}")
