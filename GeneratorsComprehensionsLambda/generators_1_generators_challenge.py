# The challenge is to create a program that will return an infinite sequence
# of odd numbers, starting at 1. Below I created two functions, each one
# representing a different solution


def odds_generator():
    current_odd = 1
    while True:
        yield current_odd
        current_odd += 2


def odds_generator_2():
    number = 0
    while True:
        number += 1
        if number % 2 != 0:
            yield number


next_odd = odds_generator_2()

for i in range(40):
    print(next(next_odd))