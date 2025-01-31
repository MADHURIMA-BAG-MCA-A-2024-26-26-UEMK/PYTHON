# Function to remove duplicates from a string
def remove_duplicates(string):
    return ''.join(sorted(set(string), key=string.index))

# Function to reverse words in a string
def reverse_words(string):
    words = string.split()
    return ' '.join(reversed(words))

# Function to print even-length words in a string
def print_even_length_words(string):
    words = string.split()
    return [word for word in words if len(word) % 2 == 0]

# Function to remove the ith character from the string
def remove_ith_character(string, i):
    return string[:i] + string[i+1:]

# Function to check if a string is palindrome
def is_palindrome(string):
    return string == string[::-1]

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Function to replace all characters of a string except the given character
def replace_except_char(string, char):
    return ''.join([c if c == char else '*' for c in string])

# Main program
def main():
    print("Choose an operation:")
    print("1. Remove duplicates from a string")
    print("2. Reverse words in a string")
    print("3. Print even length words in a string")
    print("4. Remove ith character from a string")
    print("5. Check whether a string is palindrome")
    print("6. Check if two strings are anagrams")
    print("7. Replace all characters of a string except the given character")
    
    choice = int(input("Enter your choice (1-7): "))
    
    if choice == 1:
        string = input("Enter a string: ")
        print("String after removing duplicates:", remove_duplicates(string))
    
    elif choice == 2:
        string = input("Enter a string: ")
        print("Reversed words:", reverse_words(string))
    
    elif choice == 3:
        string = input("Enter a string: ")
        print("Even length words:", print_even_length_words(string))
    
    elif choice == 4:
        string = input("Enter a string: ")
        i = int(input("Enter the index to remove: "))
        print("String after removing the ith character:", remove_ith_character(string, i))
    
    elif choice == 5:
        string = input("Enter a string: ")
        if is_palindrome(string):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    
    elif choice == 6:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        if are_anagrams(str1, str2):
            print("The strings are anagrams.")
        else:
            print("The strings are not anagrams.")
    
    elif choice == 7:
        string = input("Enter a string: ")
        char = input("Enter the character to keep: ")
        print("String after replacement:", replace_except_char(string, char))
    
    else:
        print("Invalid choice! Please choose a valid option (1-7).")

# Run the program
if __name__ == "__main__":
    main()
