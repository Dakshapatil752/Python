
def greet():
    """Simple function with no arguments."""
    print("Hello from greet()")

def add(a, b):
    """Function with positional arguments and a return value."""
    return a + b

def power(base, exponent=2):
    """Function with a default argument."""
    return base ** exponent

def describe_person(name, age=None):
    """Function with a keyword (optional) argument."""
    if age:
        print(f"{name} is {age} years old")
    else:
        print(f"{name}'s age is not provided")

def var_args(*args, **kwargs):
    """Function demonstrating *args and **kwargs."""
    print("Positional args:", args)
    print("Keyword args:", kwargs)

# Lambda example
square = lambda x: x * x

def apply_operation(a, b, func):
    """Higher-order function: takes another function as argument."""
    return func(a, b)

def main():
    print("--- greet ---")
    greet()

    print("--- add ---")
    print("2 + 3 =", add(2, 3))

    print("--- power ---")
    print("5^2 =", power(5))
    print("5^3 =", power(5, 3))

    print("--- describe_person ---")
    describe_person("Alice", 30)
    describe_person("Bob")

    print("--- var_args ---")
    var_args(1, 2, 3, name="Charlie", city="Delhi")

    print("--- lambda square ---")
    print("square(6) =", square(6))

    print("--- apply_operation with a lambda ---")
    print("3 * 4 =", apply_operation(3, 4, lambda x, y: x * y))

    print("--- apply_operation with a named function ---")
    print("10 + 20 =", apply_operation(10, 20, add))

if __name__ == '__main__':
    main()
