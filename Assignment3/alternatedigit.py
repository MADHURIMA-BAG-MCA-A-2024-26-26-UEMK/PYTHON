# Write a program to input a 10 digit number and print alternate digits.

def print_alternate_digits(number):
    # Convert the number to a string to access each digit
    digits = str(number)
    
    # Ensure the number has exactly 10 digits
    if len(digits) != 10:
        print("Please enter a valid 10-digit number.")
        return
    
    # Extract alternate digits (i.e., digits at indices 0, 2, 4, 6, 8)
    alternate_digits = digits[::2]
    
    # Print the alternate digits
    print(f"Alternate digits: {alternate_digits}")

# Input: A 10-digit number
number = input("Enter a 10-digit number: ")

# Call the function to print alternate digits
print_alternate_digits(number)
