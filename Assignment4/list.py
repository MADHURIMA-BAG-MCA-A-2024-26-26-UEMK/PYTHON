# Function to interchange the first and last elements in a list
def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Function to clone or copy a list
def clone_list(lst):
    return lst[:]

# Function to count occurrences of elements in a list
def count_occurrences(lst):
    return {item: lst.count(item) for item in set(lst)}

# Function to remove multiple elements from a list
def remove_multiple_elements(lst, elements_to_remove):
    return [item for item in lst if item not in elements_to_remove]

# Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Function to find the second largest number in a list
def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()
    if len(unique_lst) > 1:
        return unique_lst[-2]
    return None

# Function to find the intersection of two lists
def intersection_of_lists(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Function to check if two lists are identical
def are_identical(lst1, lst2):
    return lst1 == lst2

# Function to find the maximum and minimum element's position in a list
def max_min_positions(lst):
    max_pos = lst.index(max(lst))
    min_pos = lst.index(min(lst))
    return max_pos, min_pos

# Main program to demonstrate all tasks
def main():
    print("Choose an operation:")
    print("1. Interchange first and last elements in a list")
    print("2. Clone or copy a list")
    print("3. Count occurrences of elements in a list")
    print("4. Remove multiple elements from a list")
    print("5. Remove duplicates from a list")
    print("6. Find second largest number in a list")
    print("7. Intersection of two lists")
    print("8. Check if two lists are identical")
    print("9. Maximum and minimum element's position in a list")
    
    choice = int(input("Enter your choice (1-9): "))
    
    if choice == 1:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        print("List after interchanging first and last elements:", interchange_first_last(lst))
    
    elif choice == 2:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        print("Cloned list:", clone_list(lst))
    
    elif choice == 3:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        print("Occurrences of elements:", count_occurrences(lst))
    
    elif choice == 4:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        elements_to_remove = list(map(int, input("Enter elements to remove (separated by space): ").split()))
        print("List after removal:", remove_multiple_elements(lst, elements_to_remove))
    
    elif choice == 5:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        print("List after removing duplicates:", remove_duplicates(lst))
    
    elif choice == 6:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        print("Second largest number:", second_largest(lst))
    
    elif choice == 7:
        lst1 = list(map(int, input("Enter the first list: ").split()))
        lst2 = list(map(int, input("Enter the second list: ").split()))
        print("Intersection of lists:", intersection_of_lists(lst1, lst2))
    
    elif choice == 8:
        lst1 = list(map(int, input("Enter the first list: ").split()))
        lst2 = list(map(int, input("Enter the second list: ").split()))
        if are_identical(lst1, lst2):
            print("The two lists are identical.")
        else:
            print("The two lists are not identical.")
    
    elif choice == 9:
        lst = list(map(int, input("Enter a list of numbers: ").split()))
        max_pos, min_pos = max_min_positions(lst)
        print("Maximum element's position:", max_pos)
        print("Minimum element's position:", min_pos)
    
    else:
        print("Invalid choice! Please choose a valid option (1-9).")

# Run the program
if __name__ == "__main__":
    main()
