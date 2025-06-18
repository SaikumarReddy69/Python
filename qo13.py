#13. what is the difference between is and ==for string ? what is the syntax?



### 1. `==` (Equality Operator)

# Checks if the values are equal.Compares the content of two strings.


a = "hello"
b = "hello"

print(a == b)  #  True (because both have the same value)


### 🔍 **2. `is` (Identity Operator)**

# Checks **if both variables point to the same memory location**.
# Compares the **identity**, not the value.


a = "hello"
b = "hello"

print(a is b)  # ✅ True (same object in memory, due to string interning)

#But if you force different objects:


a = str("hello")
b = str("hello")

print(a == b)  #  True (same value)
print(a is b)  #  False (different objects)

