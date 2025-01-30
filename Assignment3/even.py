# 4.Write a program, which will find all such numbers between 1000 and 3000 such that each digit of the number is an even number.

def find_even_digit_numbers():
    # List to store numbers with all even digits
    even_digit_numbers = []
    
    # Loop through all numbers between 1000 and 3000
    for num in range(1000, 3001):
        # Convert number to string to check each digit
        num_str = str(num)
        
        # Check if all digits are even
        if all(int(digit) % 2 == 0 for digit in num_str):
            even_digit_numbers.append(num)
    
    # Print all such numbers
    print("Numbers between 1000 and 3000 with all even digits are:")
    print(even_digit_numbers)

# Call the function
find_even_digit_numbers()
