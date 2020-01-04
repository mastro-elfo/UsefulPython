from functools import wraps
import logging

"""Provides the `debugly` decorator

Use:
```py
@debugly
def foo(*args):
    pass
```

```py
class Bar(object):
    @debugly
    def method(**kwargs):
        pass
```
"""

def debugly(func):
    """Decorates functions and methods with `logging.debug`."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Before func
        logging.debug(f"{func.__qualname__}, {str(args)}, {str(kwargs)}")
        result = func(*args, **kwargs)
        # After func
        return result
    return wrapper

if __name__ == '__main__':
    logging.basicConfig(
        format = '%(asctime)s [%(levelname)s]: %(message)s',
        level = logging.DEBUG,
        filename = None
    )

    @debugly
    def foo(a, b = 1):
        print(a, b)

    foo(0, b = 1)
