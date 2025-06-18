#8. how can you convert the list of tuples in to a dictionary?

'''
You can convert a list of tuples into a dictionary using the built-in dict() function.

Each tuple should have two values: one for the key, one for the value.
'''
#Example:

data = [("a", 1), ("b", 2), ("c", 3)]

my_dict = dict(data)

print(my_dict) # Output: {'a': 1, 'b': 2, 'c':3}


