# Example of Polymorphism in Python

class Animal:
	def speak(self):
    		print("Animal speaks")

class Dog(Animal):
	def speak(self):
		print("Dog barks")

class Cat(Animal):
	def speak(self):
		print("Cat meows")

# Polymorphism: same method name, different behavior
def animal_sound(animal):
	animal.speak()

animals = [Dog(), Cat(), Animal()]
for a in animals:
	animal_sound(a)
