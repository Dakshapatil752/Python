"""
Example: Common set methods in Python
"""

my_set = {1, 2, 3}

# Add an element (similar to append for lists)
my_set.add(4)
print("After add(4):", my_set)

# Remove an element (raises error if not present)
my_set.remove(2)
print("After remove(2):", my_set)

# Discard an element (does not raise error if not present)
my_set.discard(10)
print("After discard(10):", my_set)

# Pop an element (removes and returns a random element)
popped = my_set.pop()
print("After pop():", my_set, "Popped element:", popped)

# Clear all elements
my_set.clear()
print("After clear():", my_set)
