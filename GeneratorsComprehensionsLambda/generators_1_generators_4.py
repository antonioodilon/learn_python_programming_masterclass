# Getting the odd numbers generator from generators_1_generators_challenge


def odds_generator():
    number = 0
    while True:
        number += 1
        if number % 2 != 0:
            yield number


# Now we are going to create a function that will return an approximation
# of the next value of pi, according to Leibniz' formula.


def pi_generator():
    odds = odds_generator()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


pi_approximation = pi_generator()

# The bigger the range, the closer it gets to the actual value of pi.
# Infinite generators are not useful only for mathematics, though.
for x in range(1000):
    print(next(pi_approximation))