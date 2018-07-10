def factorial(n):
    if type(n) is not int:
        raise ValueError('number must be integer')
    if n < 0:
        raise ValueError('number must be positive')
    if n == 0:
        return 1
    return n * factorial(n-1)