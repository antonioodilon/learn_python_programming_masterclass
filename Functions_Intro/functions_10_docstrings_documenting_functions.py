# See the code 5_returning_values_challenge_buchalka

# VERY IMPORTANT LESSON! ALWAYS DOCUMENT YOUR FUNCTIONS!!!
# Unpleasant truth 1: Many programmers (ourselves included) don't document
# their functions
# Unpleasant truth 2: Many programmers (ourselves included) REGRET not
# documenting their functions!
# VERY IMPORTANT LESSON! ALWAYS DOCUMENT YOUR FUNCTIONS!!!
    # -> See the end of the video number 156 (Writing a docstring), on
    # Section 6: Functions - An Introduction

import random  # You can press ctrl Q to see the documentation of a Python object


def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function will continue looping and prompting the user until a
    valid `int` is entered.

    :param prompt: The string that the user will see when they're prompted
        to enter the value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        # Hold ctrl and left click on input to see the documentation
        if temp.isnumeric():
            return int(temp)
        # else: -> not necessary, but might make the code more readable!
        print("{0} is not a valid number".format(temp))


print(input.__doc__)  # Documentation for input function
print("*" * 80)
print(get_integer.__doc__)  # Documentation for get_integer function
print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")