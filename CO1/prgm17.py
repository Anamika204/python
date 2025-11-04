my_dict={'apple':3,'banana':1,'cherry':2}
asc_dict=dict(sorted(my_dict.items()))
desc_dict=dict(sorted(my_dict.items(),reverse=True))
print("Original dictionary:",my_dict)
print("Ascending order:",asc_dict)
print("Descending order:",desc_dict)
