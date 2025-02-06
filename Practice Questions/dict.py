def sort_dicts_by_key(lst, key):
    return sorted(lst, key=lambda x: x.get(key))

# Example usage
list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
sorted_list = sort_dicts_by_key(list_of_dicts, 'age')
print(sorted_list)
