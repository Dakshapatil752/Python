fs1 = frozenset([1, 2, 3, 4, 5])
fs2 = frozenset([4, 5, 6, 7])

# Union
print("Union:", fs1 | fs2)

# Intersection
print("Intersection:", fs1 & fs2)

# Difference
print("Difference (fs1 - fs2):", fs1 - fs2)
print("Difference (fs2 - fs1):", fs2 - fs1)

# Symmetric Difference
print("Symmetric Difference:", fs1 ^ fs2)

# Membership test
print("Is 3 in fs1?", 3 in fs1)
print("Is 10 not in fs2?", 10 not in fs2)

# Note: frozenset is immutable, so you cannot add or remove elements

# fs1.add(6)  # This will raise an AttributeError
# fs1.remove(1)  # This will raise an AttributeError
