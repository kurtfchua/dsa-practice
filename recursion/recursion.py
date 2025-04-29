def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

def factorial_iter(n):
    res = 1
    while n >= 1:
        res = res * n
        n -= 1
    return res

    