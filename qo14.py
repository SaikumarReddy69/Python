#14. How does sciling works in tuple and string? what are the syntax?

#Slicing is used to extract a portion (part) of a string or tuple using indexes.

#It works the same way for both strings and tuples because both are ordered and indexable.


#Example:

text = "Python"

print(text[0:3])     # Output: 'Pyt'
print(text[::2])     # Output: 'Pto' (every 2nd character)
print(text[::-1])    # Output: 'nohtyP' (reversed)