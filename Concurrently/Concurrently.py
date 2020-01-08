"""`thread_map`, `process_map`

https://docs.python.org/3/library/concurrent.futures.html
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def thread_map(func, *iterables, **kwargs):
    """Maps `iterables` with `func` using ThreadPoolExecutor

    `**kwargs` are passed to ThreadPoolExecutor
    """
    with ThreadPoolExecutor(**kwargs) as ex:
        result = ex.map(func, *iterables)
    return result


def process_map(func, *iterables, **kwargs):
    """Maps `iterables` with `func` using ProcessPoolExecutor

    `**kwargs` are passed to ProcessPoolExecutor
    """
    with ProcessPoolExecutor(**kwargs) as ex:
        result = ex.map(func, *iterables)
    return result
