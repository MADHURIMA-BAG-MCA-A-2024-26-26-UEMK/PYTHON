# 2.Write a program to input a 10 digit number and find the digit with maximum value.

def find_max_digit(number):
    # Convert the number to a string to access each digit
    digits = str(number)
    
    # Ensure the number has exactly 10 digits
    if len(digits) != 10:
        print("Please enter a valid 10-digit number.")
        return
    
    # Find the maximum digit
    max_digit = max(digits)  # max() works on strings, and compares lexicographically
    
    print(f"The digit with the maximum value is: {max_digit}")

# Input: A 10-digit number
number = input("Enter a 10-digit number: ")

# Call the function to find the maximum digit
find_max_digit(number)
