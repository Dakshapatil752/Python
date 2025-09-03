#Examples: Using modules in Python

# Importing a built-in module
import math
print("Square root of 25:", math.sqrt(25))

# Importing a specific function from a module
from datetime import datetime
print("Current date and time:", datetime.now())


# Listing all attributes and functions in a module
print("Functions in math module:", dir(math))


"""
Example: Using a user-defined module in Python
"""

# Suppose you have a file named mymodule.py with the following content:
# def greet(name):
#     return f"Hello, {name}!"

# You can import and use it like this:
import mymodule
print(mymodule.greet("Alice"))
