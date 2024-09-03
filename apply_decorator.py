#decorator function that takes another function as an argument
def decorator_func(func):
    # Define a wrapper function that will be executed in place of the original function
    def wrapper(*args, **kwargs):
        # Print a message indicating that the decorator has been applied
        print("Decorator Applied")
        # Call the original function with any arguments it was given and return its result
        return func(*args, **kwargs)
    # Return the wrapper function, effectively replacing the original function with this new behavior
    return wrapper

# Define a function that applies the decorator to another function
def apply_decorator(func):
    # Apply the decorator to the input function and return the decorated function
    return decorator_func(func)