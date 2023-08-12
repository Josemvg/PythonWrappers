import functools
import time

def retry_on_error(max_retries, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Retry a function if an error occurs.

            Parameters
            ----------
            max_retries : int
                The maximum number of retries.
            delay : int, optional
                The delay between retries, by default 1.
            
            Returns
            -------
            result : any
                The result of the function. Same as the function's return value.
            """
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    retries += 1
                    time.sleep(delay)
            return None
        return wrapper
    return decorator