def check_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("x doit être positif")
        return func(x)
    return wrapper

@check_positive
def double(x):
    return x * 2

assert double(5) == 10
try:
    double(-1)
except ValueError:
    print("Exception levée correctement")