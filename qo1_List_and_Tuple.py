#Q1. Difference between list and Tuple in python?

'''
The difference between list and tuple in Python is as follows:

Mutability:

List: Mutable (can be changed after creation).
Tuple: Immutable (cannot be changed after creation).
Syntax:

List: Defined using square brackets [].
Tuple: Defined using parentheses ().
Performance:

Tuple: Generally faster than lists due to immutability.
List: Slightly slower because of mutability.
Use cases:

List: Used when you need a collection that can be modified.
Tuple: Used when you want a fixed collection of items.
Examples:
'''

#List example:

my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
print(my_list)   # Output: [10, 2, 3]

#Tuple example:

my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise a TypeError
print(my_tuple)    # Output: (1, 2, 3)