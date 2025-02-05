tup = tuple(input("Enter elements : ").split())
print("Original tuple:", tup)
tup_lst = list(tup)
print("Converted to list:", tup_lst)
i = int(input("Enter the index to modify (0-4): "))
val = input("Enter the new value: ")
tup_lst[i] = val
mod_tup = tuple(tup_lst)
print("Modified Tuple:", mod_tup)
