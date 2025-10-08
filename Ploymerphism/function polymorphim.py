# Example of Function Polymorphism in Python

def add(a, b, c=0):
	return a + b + c

print(add(2, 3))        # Output: 5
print(add(2, 3, 4))     # Output: 9

# Another example: function working with different types
def length(item):
	return len(item)

print(length([1, 2, 3]))      # Output: 3 (list)
print(length("hello"))       # Output: 5 (string)
