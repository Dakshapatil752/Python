# Example: super() with polymorphism

class Animal:
	def speak(self):
		print("Animal makes a sound")

class Dog(Animal):
	def speak(self):
		super().speak()  # Call parent class method
		print("Dog barks")

class Cat(Animal):
	def speak(self):
		super().speak()  # Call parent class method
		print("Cat meows")

# Polymorphism: same method name, different behavior
def animal_sound(animal):
	animal.speak()

animals = [Dog(), Cat()]
for a in animals:
	animal_sound(a)
