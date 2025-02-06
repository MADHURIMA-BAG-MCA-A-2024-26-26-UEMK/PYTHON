def check_key(d, key):
 return key in d
dict = {"name": "Alice", "age": 25}
print("Does 'age' exist in dictionary? : ", check_key(dict, "age"))
