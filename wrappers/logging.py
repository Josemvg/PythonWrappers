import logging
import functools

def log_function(func):
    logging.basicConfig(level=logging.INFO)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Log the function call and return value.

        Parameters
        ----------
        func : function
            The function to be logged.
        
        Returns
        -------
        result : any
            The result of the function. Same as the function's return value.
        """
        args_str = ', '.join([repr(arg) for arg in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()])
        logging.info(f"Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {repr(result)}")
        return result
    return wrapper