def gcd(a, b):
    # Base case: If b is 0, return a
    if b == 0:
        return a
    # Recursive case: Call gcd(b, a % b)
    return gcd(b, a % b)

# Calling the function with two numbers
print(gcd(48, 18))
