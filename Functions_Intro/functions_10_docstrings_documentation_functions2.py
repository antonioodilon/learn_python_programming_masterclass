# See the code 5_returning_values_challenge

# VERY IMPORTANT LESSON! ALWAYS DOCUMENT YOUR FUNCTIONS!!!
# Unpleasant truth 1: Many programmers (ourselves included) don't document
# their functions
# Unpleasant truth 2: Many programmers (ourselves included) REGRET not
# documenting their functions!
# VERY IMPORTANT LESSON! ALWAYS DOCUMENT YOUR FUNCTIONS!!!
    # -> See the end of the video number 156 (Writing a docstring), on
    # Section 6: Functions - An Introduction

import random


def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function will continue looping and prompting the user until a
    valid `int`, less than or equal to the highest number possible, or
    greater than or equal to 1, is entered. If the user inserts an `int`
    outside of this range, the function will ask the user to enter a
    valid number. If the user inserts a `str` instead of an `int`, the
    program will crash.

    :param prompt: The string that the user will see when they're prompted
        to enter the value
    :return: None
    """
    while True:
        temp = int(input(prompt))
        if temp == answer:
            print("Well done, you guessed it")
            break
        # elif temp == 0:
        #     break
        elif answer > temp >= 1:
            print("Please guess higher")
        elif highest >= temp > answer:
            print("Please guess lower")
        else:
            print("Please enter a valid number")
            pass


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