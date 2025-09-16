#creating a class
class Dog:
    #class attribute
    species = "canis familiaris"
    #initializer / instance attributes
    def __init__(self, name, age):
        self.name =name
        self.age =age
        #instance method
        def description(self):
            return f"{self.name} is {self.age} years old"
        def speak(self , sound):
            return f"{self.name} says {sound}"
        #instance of the class
mikey = Dog("Mikey",6)
print(f"{mikey.name} is {mikey.age} years old")
print(f"{mikey.name} is a {mikey.species}")


        
        