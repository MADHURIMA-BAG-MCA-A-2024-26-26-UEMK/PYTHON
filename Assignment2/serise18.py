#  Find the nth term a,b,b,c,c,c,……………………
import string

def nth_term(n):
    # Calculate the group number where the nth term belongs
    group = 1
    total_terms = 0
    
    while total_terms + group < n:
        total_terms += group
        group += 1
    
    # The character that corresponds to the group number
    # The groups start at 1 for 'a', 2 for 'b', 3 for 'c', and so on
    character = string.ascii_lowercase[group - 1]
    
    return character

# Example usage:
n = 7  # You can change n to find the nth term
result = nth_term(n)
print(f"The {n}th term of the sequence is: {result}")
