nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
second_element = nested_tuple[1][1]
print(f"Second element of second inner tuple: {second_element}")
last_element = nested_tuple[2][-1]
print(f"Last element of third inner tuple: {last_element}")
print(f"First inner tuple: {nested_tuple[0]}")
print(f"Second inner tuple: {nested_tuple[1]}")
print(f"Third inner tuple: {nested_tuple[2]}")
