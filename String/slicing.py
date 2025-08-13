"""
Examples: Different types of string slicing in Python
"""

my_str = "Programming"

# Basic slicing
print("Characters from index 0 to 4:", my_str[0:5])

# Slicing from start to a specific index
print("First 7 characters:", my_str[:7])

# Slicing from a specific index to end
print("Characters from index 3 to end:", my_str[3:])

# Slicing with step
print("Every second character:", my_str[::2])

# Slicing with negative step (reverse)
print("Reversed string:", my_str[::-1])

# Slicing a substring in the middle
print("Characters from index 2 to 7:", my_str[2:8])

# Slicing with negative indices
print("Last 4 characters:", my_str[-4:])
print("All except last 3 characters:", my_str[:-3])
