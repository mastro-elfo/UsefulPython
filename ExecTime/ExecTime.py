"""Measures the execution time.

Modifies the values returned by the non decorated function so that the first value is the measure and the second value is what the function returned.
"""

from functools import wraps
from time import perf_counter

def ExecTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before func
        start_time = perf_counter()
        result = func(*args, **kwargs)
        # After func
        time_diff = perf_counter() - start_time
        return (time_diff, result)

    return wrapper
