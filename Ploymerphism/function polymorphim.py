# Example of Function Polymorphism in Python

def add(a, b, c=0):
	return a + b + c

print(add(2, 3))      
print(add(2, 3, 4))     

# Another example: function working with different types
def length(item):
	return len(item)

print(length([1, 2, 3]))      
print(length("hello"))      
