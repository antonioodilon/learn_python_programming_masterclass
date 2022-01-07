a = 2
b = 3
print("a is {0}, b is {1}". format(a, b))

# This is a good and useful way to swap values in Python.
a, b = b, a
# This is the same as typing a, b = 3, 2
print("a is {0}, b is {1}". format(a, b))

# Now we are going to use the above technique to return the Fibonacci numbers:


def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()

# Printing the first 10 fibonacci numbers. Each time we call the function
# through the variable fib, it returns the next fibonacci number. If you
# don't store it inside a variable and call the function directly, it will
# just print 1 every time.
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))