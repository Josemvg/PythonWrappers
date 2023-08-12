import time
import functools

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Measure the execution time of a function.

        Parameters
        ----------
        func : function
            The function to be measured.
        
        Returns
        -------
        result : any
            The result of the function. Same as the function's return value.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds.")
        return result
    return wrapper