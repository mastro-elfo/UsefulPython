from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before func
        result = func(*args, **kwargs)
        # After func
        return result
    return wrapper
