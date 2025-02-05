def check_membership(t, element):
 return element in t
tup = tuple(input("Enter elements : ").split())
s_ele = input("Enter element to search: ")
r = check_membership(tup, s_ele)
print(f"Is {s_ele} present in tuple? : {r}")