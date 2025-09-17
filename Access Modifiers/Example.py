# Example demonstrating public, protected, and private access modifiers
class Person:
    def __init__(self, name, age, country):
        self.name = name           # Public attribute
        self._country = country    # Protected attribute
        self.__age = age           # Private attribute

    def get_age(self):
        return self.__age          # Access private attribute inside the class

class Student(Person):
    def show(self):
        print("Name (public):", self.name)            # Accessing public attribute
        print("Country (protected):", self._country)  # Accessing protected attribute
        # print("Age (private):", self.__age)         # This would raise an AttributeError
        print("Age (private via getter):", self.get_age())

s = Student("SDP", 21, "India")
s.show()

# Accessing public attribute (allowed)
print(s.name)
# Accessing protected attribute (allowed, but not recommended)
print(s._country)

class Person:
    def __init__(self, name, age):
        self._name = name           # Protected attribute
        self.__age = age            # Private attribute

    def get_age(self):
        return self.__age           # Access private attribute inside the class

class Student(Person):
    def show(self):
        print("Name (protected):", self._name)  # Accessing protected attribute
        # print("Age (private):", self.__age)   
        print("Age (private via getter):", self.get_age())

s = Student("Alice", 21)
s.show()

# Accessing protected attribute (not recommended, but possible)
print(s._name)

