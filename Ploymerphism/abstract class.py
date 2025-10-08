# Example of Abstract Class in Python
from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def speak(self):
		pass

class Dog(Animal):
	def speak(self):
		print("Dog barks")

class Cat(Animal):
	def speak(self):
		print("Cat meows")

# Example usage
d = Dog()
d.speak()
c = Cat()
c.speak()
