# non local => create and change names in an enclosing scope
# nonlocal chose the scope from local to the enlosing scope

def outer():
    """Prints the value of n."""
    n = 1
    print(n)
    def inner():
        nonlocal n
        n = 2
        print(n)

    inner()
    print(n)


outer()