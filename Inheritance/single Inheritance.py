# Single Inheritance Example: Animal -> Dog

class Animal:
	def __init__(self, name):
		self.name = name
	def display(self):
		print(f"Animal name: {self.name}")

class Dog(Animal):
	def getname(self):
		return self.name

# Example usage
d = Dog("Tommy")
d.display()
print("Dog's name (using getname):", d.getname())
