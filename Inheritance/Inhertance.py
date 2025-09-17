	# Example demonstrating single, multilevel, multiple, and hybrid inheritance with Student class

	# Single Inheritance: Student inherits from Person
class Person:
	def show(self):
		print("I am a person.")

class Student(Person):  # Single Inheritance
	def display(self):
		print("I am a student.")

	# Multilevel Inheritance: Graduate inherits from Student, which inherits from Person
class Graduate(Student):  # Multilevel Inheritance
	def info(self):
		print("I am a graduate student.")

	# Multiple Inheritance: Sports inherits from both Student and Marks
class Marks:
	def marks(self):
		print("I have marks.")

class Sports(Student, Marks):  # Multiple Inheritance
	def sports_info(self):
		print("I play sports.")

	# Hybrid Inheritance: Scholar inherits from Graduate and Sports
class Scholar(Graduate, Sports):  # Hybrid Inheritance
	def scholar_info(self):
		print("I am a scholar student.")

	# Create object of Scholar to demonstrate all inheritance types
s = Scholar()
s.show()           # From Person (single, multilevel, hybrid)
s.display()        # From Student (single, multilevel, multiple, hybrid)
s.info()           # From Graduate (multilevel, hybrid)
s.marks()          # From Marks (multiple, hybrid)
s.sports_info()    # From Sports (multiple, hybrid)
s.scholar_info()   # From Scholar (hybrid)
