from functools import wraps
import logging

"""Provides handy functions for logging.

Example
```py
from Log import debug, info, warning, error, critical

debug("Some message %s", str(value))
```
"""

logging.basicConfig(
    format = '%(asctime)s [%(levelname)s]: %(message)s',
    level = logging.DEBUG,
    filename = None)

def log(severity, *args, **kwargs):
    return severity(*args, **kwargs)

def debug(*args, **kwargs):
    """Logs a debug line"""
    return log(logging.debug, *args, **kwargs)

def info(*args, **kwargs):
    """Logs an info line"""
    return log(logging.info, *args, **kwargs)

def warning(*args, **kwargs):
    """Logs a warning line"""
    return log(logging.warning, *args, **kwargs)

def error(*args, **kwargs):
    """Logs an error line"""
    return log(logging.error, *args, **kwargs)

def critical(*args, **kwargs):
    """Logs a critical line"""
    return log(logging.critical, *args, **kwargs)

if __name__ == '__main__':
    debug("Debug")
    info("Info")
    warning("Warning")
    error("Error")
    critical("Critical")
