import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} sec")
        return result
    return wrapper

@timer
def compute():
    time.sleep(1)
    return "Done"

print(compute())
