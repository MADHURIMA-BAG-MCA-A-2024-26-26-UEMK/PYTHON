# 1.Write a program to input a 4 digit number and print the even and odd digits and total even and odd digits

def categorize_digits(number):
    # Convert the number to a string to access each digit
    digits = str(number)
    
    # Initialize lists to store even and odd digits
    even_digits = []
    odd_digits = []
    
    # Loop through each digit in the string representation of the number
    for digit in digits:
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    
    # Print the even and odd digits
    print("Even digits:", " ".join(even_digits))
    print("Odd digits:", " ".join(odd_digits))
    
    # Print the total count of even and odd digits
    print(f"Total even digits: {len(even_digits)}")
    print(f"Total odd digits: {len(odd_digits)}")

# Input: A 4-digit number
number = int(input("Enter a 4-digit number: "))

# Call the function to categorize and print the digits
categorize_digits(number)
