#10. can we use a list as a key in a dictionary? why and why not?


'''
No, you cannot use a list as a key in a dictionary.

Reason:

Dictionary keys must be immutable and hashable.

A list is mutable(you can change its contents).
Therefore, lists are not hashable and cannot be used as keys.
'''
#Example:


my_dict = {[1, 2]: "value"}  #  Error Output: TypeError: unhashable type: 'list'


#What can be used as keys
'''
* Strings → ✅
* Numbers → ✅
* Tuples (if all elements are immutable) → ✅
* Lists → ❌
'''
### ✅ Example Using Tuple as a Key:


my_dict = {(1, 2): "value"}  # ✅ Works
print(my_dict[(1, 2)])       # Output: value


