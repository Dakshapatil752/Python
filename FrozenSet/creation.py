"""
Examples: Creation of frozenset in Python
"""

# Creating a frozenset from a list
fs1 = frozenset([1, 2, 3, 4])
print("Frozenset from list:", fs1)

# Creating a frozenset from a tuple
fs2 = frozenset((10, 20, 30))
print("Frozenset from tuple:", fs2)

# Creating a frozenset from a set
fs3 = frozenset({100, 200, 300})
print("Frozenset from set:", fs3)

# Creating a frozenset from a string (each character becomes an element)
fs4 = frozenset("hello")
print("Frozenset from string:", fs4)

# Creating an empty frozenset
fs_empty = frozenset()
print("Empty frozenset:", fs_empty)
