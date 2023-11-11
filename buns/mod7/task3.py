import time

def calculate_fibonacci(n):
    if n < 2:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

def validate_arguments(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapper

def memoization_decorator(func):
    memoization_cache = {}

    def wrapper(*args):
        if args in memoization_cache:
            return memoization_cache[args]
        result = func(*args)
        memoization_cache[args] = result
        return result

    return wrapper

class TimingDecorator:
    def __init__(self):
        self.active = False

    def __call__(self, func):
        def wrapper(*args):
            if self.active:
                return func(*args)
            start_time = time.time()
            self.active = True
            result = func(*args)
            end_time = time.time()
            self.active = False
            return result, end_time - start_time

        return wrapper
