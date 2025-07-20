       n_tuple = (4, 10, 12, 16)
print("New Tuple:", n_tuple)
m_list = list(n_tuple)
m_list[1] = 10
my_tuple = tuple(m_list)
print("Modified Tuple via List:", my_tuple)
