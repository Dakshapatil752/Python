"""
Examples: Lambda functions in Python
"""

# Simple lambda function for addition
add = lambda x, y: x + y
print("Addition using lambda:", add(5, 3))

# Lambda for squaring a number
square = lambda x: x ** 2
print("Square using lambda:", square(4))

# Lambda for checking even or odd
is_even = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print("Check even/odd using lambda:", is_even(7))

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map and lambda:", squares)

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter and lambda:", even_numbers)

# Using lambda with sorted() for custom sorting
pairs = [(2, 5), (1, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Pairs sorted by second element:", sorted_pairs)
