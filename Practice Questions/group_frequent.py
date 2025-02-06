from collections import Counter

def group_by_frequency(lst):
    freq = Counter(lst)
    grouped = {}
    
    for key, value in freq.items():
        if value not in grouped:
            grouped[value] = []
        grouped[value].append(key)
    
    return grouped

# Example usage
my_list = [1, 2, 2, 3, 3, 3, 4]
print(group_by_frequency(my_list))
