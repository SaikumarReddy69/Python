#2. How do set helps in removing duplicates from the list?

#Sets in Python help in removing duplicates from a list because sets automatically store only unique elements. When you convert a list to a set, all duplicate elements are removed. You can then convert the set back to a list if needed.

#Example:

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)  # Convert list to set to remove duplicates
unique_list = list(my_set)  # Convert set back to list
print(unique_list)  # Output: [1, 2, 3, 4, 5]