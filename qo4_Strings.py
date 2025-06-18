#4. How are python strings immutable if they allow operations like replace() ?

'''
 Immutable means you cannot change the original string.

But when you use methods like `replace()`, Python **creates a new string** instead of changing the original one.

'''
###Example:
name = "hello"
new_name = name.replace("h", "y")

print(name)      # Output: hello (original string is unchanged)
print(new_name)  # Output: yello (new string is created)

