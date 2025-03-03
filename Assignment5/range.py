# Function to check whether a number is within a specified range
def is_within_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False

# Accepting inputs from the user
number = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Calling the function and printing the result
if is_within_range(number, start, end):
    print(f"The number {number} is within the range {start} to {end}.")
else:
    print(f"The number {number} is NOT within the range {start} to {end}.")
