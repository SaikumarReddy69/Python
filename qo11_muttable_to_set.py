#11. what happens if you try add a mutable object to set?



###  You cannot add mutable objects (like lists or dictionaries) to a set.

###  Why?
'''
Because:

* Sets only allow items that **cannot change** (called **immutable**).
* Lists and dictionaries **can change**, so Python gives an error.
'''

###  Example:

my_set = set()
my_set.add([1, 2, 3])  #  Error Output: TypeError: unhashable type: 'list'


###  What works:

my_set = set()
my_set.add((1, 2, 3))  # ✅ Tuple is allowed
print(my_set)   #**Output:**{(1, 2, 3)}




