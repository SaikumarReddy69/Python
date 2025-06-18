#9. how would you handle missing Key in a dictionary ?

my_dict = {"a": 1}
print(my_dict.get("b"))           # Output: None
print(my_dict.get("b", 0))        # Output: 0 (default value)
