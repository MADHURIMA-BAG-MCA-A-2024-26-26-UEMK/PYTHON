# Write a program to input a string and a number to encode the string by adding the number to every character in the string

# Function to encode the string by adding the number to ASCII value of each character
def encode_string(string, number):
    encoded_string = ""
    
    # Loop through each character in the string
    for char in string:
        # Add the number to the ASCII value of the character and convert it back to a character
        encoded_char = chr(ord(char) + number)
        encoded_string += encoded_char
    
    return encoded_string

# Input the string and the number
user_input = input("Enter a string: ")
shift_value = int(input("Enter a number to encode the string: "))

# Get the encoded string
encoded_string = encode_string(user_input, shift_value)

# Output the encoded string
print("Encoded string:", encoded_string)
