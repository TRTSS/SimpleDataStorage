from functools import wraps


def secure_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("HELLO SECURE")
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper
