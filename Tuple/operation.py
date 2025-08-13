"""
Examples: Various operations on tuples in Python
"""

tup = (10, 20, 30, 40, 50)

# Accessing elements
print("First element:", tup[0])
print("Last element:", tup[-1])

# Slicing
print("Elements from index 1 to 3:", tup[1:4])

# Length of tuple
print("Length:", len(tup))

# Concatenation
tup2 = (60, 70)
print("Concatenation:", tup + tup2)

# Repetition
print("Repetition:", tup * 2)

# Membership test
print("Is 30 in tuple?", 30 in tup)
print("Is 100 not in tuple?", 100 not in tup)

# Iterating through tuple
for item in tup:
    print("Item:", item)

# Finding index of an element
print("Index of 40:", tup.index(40))

# Counting occurrences of an element
print("Count of 20:", tup.count(20))
