from collections import Counter

def most_frequent_element(lst):
    counter = Counter(lst)
    return counter.most_common(1)[0]

# Example usage
my_list = [1, 2, 2, 3, 3, 3, 4]
print(most_frequent_element(my_list))
