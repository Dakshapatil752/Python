# destructor in python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} is being deleted")

p1 = Person("xyz", 30)
print(p1.name)
print(p1.age)
del p1  
