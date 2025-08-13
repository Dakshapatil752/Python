"""
Examples: Different dictionary methods in Python
"""

my_dict = {'name': 'Bob', 'age': 30, 'city': 'London'}

# Accessing keys
print("Keys:", my_dict.keys())

# Accessing values
print("Values:", my_dict.values())

# Accessing items
print("Items:", my_dict.items())

# Getting a value with get()
print("Get age:", my_dict.get('age'))
print("Get country (default):", my_dict.get('country', 'Unknown'))

# Adding or updating an item
my_dict['age'] = 31
print("After updating age:", my_dict)

# Removing an item with pop()
popped = my_dict.pop('city')
print("After pop('city'):", my_dict, "Popped value:", popped)

# Removing last item with popitem()
last = my_dict.popitem()
print("After popitem():", my_dict, "Last item:", last)

# Clearing all items
my_dict.clear()
print("After clear():", my_dict)

# Copying a dictionary
new_dict = {'x': 1, 'y': 2}
copied = new_dict.copy()
print("Copied dictionary:", copied)
