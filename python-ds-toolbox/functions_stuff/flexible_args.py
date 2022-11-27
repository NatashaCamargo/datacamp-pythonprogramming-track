def add_all(*args):
    # * pass all arguments of a function call into a tupple called argsin the fcn body
    # then we initialize the sum and loop throug args 
    """Sum all values in *args together."""

    # Initialize sum
    sum_all = 0

    # Accumulate the sum
    for num in args:
        sum_all += num

    return sum_all


# output examples
print(add_all(1))

print(add_all(1, 2))

print(add_all(5, 10, 15, 20))

def print_all(**kwargs):
    """Print out key-value pairs in **kwargs"""

    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)


print_all(name="dumbledore", job="headmaster")