# Function to check whether a number is perfect or not
def is_perfect_number(number):
    # Calculate the sum of divisors excluding the number itself
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors equals the number
    if sum_of_divisors == number:
        return True
    else:
        return False

# Accepting input from the user
number = int(input("Enter a number to check if it's perfect: "))

# Calling the function and printing the result
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
