# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit


fact_function = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
"""


factorial_function = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
"""


setup = """\
gc.enable()
for n in range(1, 51):
    print(fact(n))

for m in range(1, 51):
    print(factorial(m))
"""


result_1 = timeit.timeit(fact_function, globals=globals(), number=1000)
result_2 = timeit.timeit(factorial_function, globals=globals(), number=1000)

print("Result 1 is: ", result_1)
print("Result 2 is: ", result_2)