keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
if len(keys) == len(values):
 conv_dict = {k: v for k, v in zip(keys, values)}
 print("Converted Dictionary:", conv_dict)
else:
 print("Error.")