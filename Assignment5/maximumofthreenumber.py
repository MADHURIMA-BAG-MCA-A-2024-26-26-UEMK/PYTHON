# Function to find the maximum of three numbers
def find_maximum(num1, num2, num3):
    # Using the built-in max function to find the maximum
    return max(num1, num2, num3)

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calling the function and printing the result
maximum = find_maximum(num1, num2, num3)
print(f"The maximum of the three numbers is: {maximum}")
