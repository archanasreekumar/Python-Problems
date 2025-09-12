def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    print(a + b)

add(5, 3)
