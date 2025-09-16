# default constructor
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("abc", 30)
print(p1.name)
print(p1.age)
p2 =person("xyz",25)
print(p2.age)
print(p2.name)
