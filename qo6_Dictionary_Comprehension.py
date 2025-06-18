#6. Explain dictionary comprehension with example?
'''
Dictionary comprehension is a concise way to create dictionaries in Python using a single line of code. It follows the syntax:

python
{key_expression: value_expression for item in iterable if condition}
Example: Creating a dictionary from a list
Let’s say we have a list of numbers and we want to create a dictionary where each number is the key, and its square is the value:
'''


numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict)     #Otput:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

