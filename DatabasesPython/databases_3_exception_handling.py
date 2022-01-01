def factorial(n):
    # n! can be defined as n * (n-1)
    if n <= 1:
        return n
    else:
        # print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(100))
except (RecursionError, OverflowError):  # Write the name of the error here. So pay close attention
    # to the type of error the output shows
    # According to Tim, it is very unlikely that we'll have an OverflowError
    # in Python. I'm just mentioning this error here out of curiosity.
    print("This program cannot handle factorials that large")
except ZeroDivisionError:
    print("It is impossible to divide by zero")
# except (RecursionError, ZeroDivisionError):
#     print("An error has happened. Please check your input again")
# It can be useful to have one except clause that handles more than one exception,
# but in our case it isn't useful.

print("Program terminating")