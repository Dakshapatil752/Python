class MyClass:
    def __init__(self):
        self.__private_var = 10  # Private variable

    def get_private_var(self):
        return self.__private_var  # Accessing private variable inside the class

obj = MyClass()
print(obj.get_private_var())    