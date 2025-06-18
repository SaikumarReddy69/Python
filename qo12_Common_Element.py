#12. write a code to find common elements in two lists using set operations?



list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets and use intersection
common = set(list1) & set(list2)

print("Common elements:", list(common)) #Output:Common elements: [4, 5]