def fizz_buzz(number: int) -> str:  # Remember to always annotate the
    # function's parameters!
    """
    Returns the `strings` `fizz`, `buzz` or `fizz buzz` in case the number
    in a certain range is divisible by 3 and not 15, 5 and not 15, or
    3 and 5 (15), respectively.
    :param number: `int`, the number to check
    :return: `str` `fizz` if divisible by 3
            `str` `buzz` if divisible by 5
             or `str` `fizz buzz` if divisible by 3 and 5 (15)
    """
    if number % 3 == 0 and number % 15 != 0:
        return "fizz"
    elif number % 5 == 0 and number % 15 != 0:
        return "buzz"
    elif number % 15 == 0:
        return "fizz buzz"
    else:
        return str(number)  # The return must always be a number!


next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose. Try again next time.")
        break
else:
    print("Congratulations for finishing the game!")
# Now I understand what this game is! The player's input can be a number (an int)
# or a string ("fizz", "buzz" or "fizz buzz")