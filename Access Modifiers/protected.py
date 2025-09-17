class Parent:
    def __init__(self):
        self._protected_var = 20  # Protected variable

class Child(Parent):
    def show_protected(self):
        print("Protected variable from Child:", self._protected_var)

obj = Child()
obj.show_protected()           # This works

print(obj._protected_var)      # This also works, but by convention should not be accessed directly