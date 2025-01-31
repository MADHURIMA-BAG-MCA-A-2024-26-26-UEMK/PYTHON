#  Write a program to find the frequency of characters in a given string.

# Function to find the frequency of characters
def char_frequency(string):
    freq = {}
    
    # Loop through each character in the string
    for char in string:
        # If character is already in dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If character is not in dictionary, add it with a count of 1
        else:
            freq[char] = 1
    
    return freq

# Input the string
user_input = input("Enter a string: ")

# Get the frequency of characters
frequency = char_frequency(user_input)

# Output the frequency of each character
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
