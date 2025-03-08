def power(a, b):
    # Base case: If b is 0, return 1 (as anything raised to 0 is 1)
    if b == 0:
        return 1
    # Recursive case: Multiply a with the result of power(a, b-1)
    return a * power(a, b - 1)

# Calling the function with a number and its exponent
print(power(2, 3))  # 2^3 = 8
