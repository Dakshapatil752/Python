set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", set1 | set2)

# Intersection
print("Intersection:", set1 & set2)

# Difference
print("Difference (set1 - set2):", set1 - set2)
print("Difference (set2 - set1):", set2 - set1)

# Symmetric Difference
print("Symmetric Difference:", set1 ^ set2)

# Adding an element
set1.add(6)
print("After adding 6 to set1:", set1)

# Removing an element
set1.remove(1)
print("After removing 1 from set1:", set1)

# Checking membership
print("Is 3 in set1?", 3 in set1)
print("Is 10 not in set2?", 10 not in set2)
