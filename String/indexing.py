"""
Examples: Indexing in Python using strings
"""

my_str = "Python"

# Accessing individual characters
print("First character:", my_str[0])
print("Third character:", my_str[2])
print("Last character:", my_str[-1])

# Slicing a string
print("Characters from index 1 to 3:", my_str[1:4])
print("First three characters:", my_str[:3])
print("Characters from index 2 to end:", my_str[2:])

# Reversing a string using slicing
print("Reversed string:", my_str[::-1])

# Accessing every second character
print("Every second character:", my_str[::2])
