from functools import wraps
import time

def track_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # Execute the function
        elapsed_time = time.time() - start_time # Calculate the elapsed time
        print(f"func:{func.__name__} took {elapsed_time:.2f} seconds to execute")
        return result
    return wrapper
