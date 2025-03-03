# Function to count the number of lowercase and uppercase characters
def count_case_characters(s):
    lowercase_count = 0
    uppercase_count = 0
    
    for char in s:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
    
    return lowercase_count, uppercase_count

# Accepting input from the user
string = input("Enter a string: ")

# Calling the function and getting the result
lowercase, uppercase = count_case_characters(string)

# Printing the result
print(f"Number of lowercase characters: {lowercase}")
print(f"Number of uppercase characters: {uppercase}")
