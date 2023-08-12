import functools

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Handle errors that occur in a function.

        Parameters
        ----------
        func : function
            The function to be measured.
        
        Returns
        -------
        result : any
            The result of the function. Same as the function's return value.
        """
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            result = None
        return result
    return wrapper