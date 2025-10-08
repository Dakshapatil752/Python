# Example of Method Overloading in Python

class Calculator:
	def add(self, a, b, c=0):
		return a + b + c

calc = Calculator()
print(calc.add(2, 3))     
print(calc.add(2, 3, 4))   
