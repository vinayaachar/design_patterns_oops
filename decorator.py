from functools import wraps


def make_blinks(function):
    """Define the decorator"""

    # this makes the decorator transparent in terns of its name and docs
    @wraps(function)
    # Define the inner function
    def decorator():
        """Grab the reurn value of the function being decorated"""

        ret = function()

        # Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


@make_blinks
def hello_world():
    """Returns plain string"""

    return 'Hello, World!'


print(hello_world())

# Prints function name hello world due to wraps
print(hello_world.__name__)

# Prints doc string of hello world transparently due to wraps
print(hello_world.__doc__)
