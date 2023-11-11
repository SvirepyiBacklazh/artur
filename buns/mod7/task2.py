from functools import wraps

def memoization_decorator(func):
    memoization_cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in memoization_cache:
            return memoization_cache[args]
        result = func(*args)
        memoization_cache[args] = result
        return result

    return wrapper

@memoization_decorator
def calculate_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 2:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
