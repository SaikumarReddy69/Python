#7. what are nested dictionaries and how do they you access inner values?

'''
A nested dictionary means a dictionary inside another dictionary.

It helps you store related data in a structured way.
'''
# Example:


student = {
    "name": "Rahul",
    "marks": {
        "math": 95,
        "science": 88
    }
}

print(student["marks"]["math"]) # Output: 95

