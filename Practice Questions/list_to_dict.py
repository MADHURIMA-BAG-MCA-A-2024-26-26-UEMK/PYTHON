def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

# Example usage
my_list = ['apple', 'banana', 'cherry']
print(list_to_dict(my_list))
