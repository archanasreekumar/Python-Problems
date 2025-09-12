def my_decorator(func):
    def wrapper():
        print("This happens before hello")
        func()
        print("This happens after hello")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()

