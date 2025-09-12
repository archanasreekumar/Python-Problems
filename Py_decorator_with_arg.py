def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("This happens before func")
        func(*args, **kwargs)
        print("This happens after func")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"hello {name}")

say_hello("Archana")

