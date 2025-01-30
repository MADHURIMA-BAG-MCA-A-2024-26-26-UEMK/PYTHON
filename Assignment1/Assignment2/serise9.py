#1+2+11+26+47+……………………………………………..
def sequence_sum(n):
    total = 0
    terms = []
    for i in range(1, n + 1):
        term = 3 * i**2 - 2 * i + 0  # This is the quadratic formula for the sequence
        terms.append(term)
        total += term
    return total, terms

# Example usage:
n = 10  # You can change n to the number of terms you want
result, terms = sequence_sum(n)
print(f"The first {n} terms of the series are: {terms}")
print(f"The sum of the first {n} terms is: {result}")
