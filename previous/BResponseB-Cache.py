from functools import wraps
import threading


def expensive_computation_decorator(cache):
    cache_lock = threading.Lock()  # Create a lock for thread-safe cache access

    def decorator(func):
        @wraps(func)  # Preserve the metadata of the original function
        def wrapper(*args, **kwargs):
            # Create a key based on args and kwargs to identify the result in the cache
            # For simplicity, kwargs are ignored in this example but should be considered in a complete solution
            cache_key = (args, tuple(sorted(kwargs.items())))

            # Thread-safe access to check if result is in cache
            with cache_lock:
                if cache_key in cache:
                    return cache[cache_key]

            # If not in cache, compute and store the result in a thread-safe manner
            result = func(*args, **kwargs)
            with cache_lock:
                cache[cache_key] = result
            return result

        return wrapper

    return decorator


# Applying the decorator with a cache dictionary
@expensive_computation_decorator(cache={})
def compute_expensive_operation(x):
    from time import sleep
    sleep(2)  # Simulate delay
    return x * x  # Example operation


# Example usage:
if __name__ == "__main__":
    print(compute_expensive_operation(4))  # Computed, cached, and then result returned
    print(compute_expensive_operation(4))  # Result returned from cache, no computation
