# Recursion isn't always the best idea. Sometimes the time it takes to process
# the code is increased very much, and is thus not performance-friendly.

def fact(n: int) -> int:
    """
    Calculates the factorial of n, or n!, iteratively
    :param n: int
    :return: int
    """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n: int) -> int:
    # n can also be defined as n * (n - 1). The function keeps stacking up
    # the results because it calls itself. It is as if a function was calling
    # another function, but in this case the function is itself.
    """
    Calculates the factorial of n recursively
    :param n: int
    :return: int
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    """F(n) = F(n - 1) + F(n - 2)"""
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    # This function is significantly faster than fib()
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for x in range(10):
    print(x, fact(x))

print("-" * 60)

for z in range(10):
    print(z, factorial(z))

print("-" * 60)

for j in range(30):
    print(j, fib(j))

print("-" * 60)

for k in range(30):
    print(k, fibonacci(k))