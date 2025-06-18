#3. Why are dictionaries faster than lists for lookups?

'''
Dictionaries are faster than lists for lookups because dictionaries use a hash table data structure, which allows for average O(1) time complexity for lookups. This means that accessing a value by key in a dictionary is very fast regardless of the size of the dictionary.

In contrast, lists require O(n) time complexity for lookups because they may need to be searched sequentially until the desired element is found.
'''

#Example:


# List lookup (O(n))
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # This checks each element until 3 is found

# Dictionary lookup (O(1))
my_dict = {'a': 1, 'b': 2, 'c': 3}
print('b' in my_dict)  # Directly accesses the key using hashing
