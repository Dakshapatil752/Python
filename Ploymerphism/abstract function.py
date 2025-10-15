
# Example of Abstract Class and Abstract Method in Python
from abc import ABC, abstractmethod
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass
class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self):
		return self.width * self.height
class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		import math
		return math.pi * self.radius * self.radius
# Example usage
r = Rectangle(5, 3)
print("Rectangle area:", r.area())
c = Circle(4)
print("Circle area:", c.area())
