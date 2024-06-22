import threading
from functools import wraps


def expensive_computation_decorator(cache):
    lock = threading.Lock()  # Lock object for thread safety

    def decorator(func):
        @wraps(func)  # To preserve the original function's docstring and other metadata
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)  # Create a unique key based on the arguments

            # Check if the result is already in the cache
            with lock:
                if key in cache:
                    return cache[key]

            # If not in cache, compute the result and cache it
            result = func(*args, **kwargs)
            with lock:
                cache[key] = result  # Cache the result

            return result

        return wrapper

    return decorator


@expensive_computation_decorator(cache={})
def compute_expensive_operation(x):
    from time import sleep
    sleep(2)  # Simulate delay
    return x * x  # Example operation


# Example usage:
print(compute_expensive_operation(4))  # Should compute once and cache, quickly return from cache on subsequent calls
