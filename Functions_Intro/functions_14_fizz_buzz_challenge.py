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


# user_answer = 0
print("Let's play Fizz Buzz! The program will give you a range of numbers, "
      "from 1 to 100, and will print:\n"
      "1) 'Fizz' for numbers that are divisible by 3 and only 3\n"
      "2) 'Buzz' for numbers that are divisible by 5 and only 5\n"
      "3) 'Fizz Buzz' for numbers that are divisible by 3 and 5 at the same"
      "time\n"
      "So type in the number the program just referred to! If you get it right,"
      "the program will continue until 100. If you get it wrong, you lose!")
for i in range(1, 101):
    # user_answer = 0
    print(fizz_buzz(i))
    if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
        user_answer = int(input("What is the number I have just "
                                "referred to? "))
        # fizz_buzz(int(input("What is the number I have just "
        #                     "referred to? ")))
        if user_answer == i:
            print("Congratulations! Let's move on.")
            print()
        else:
            print("I'm sorry, but your answer is wrong. The program is now "
                  "terminating.")
            break
    elif i > 100:
        print("Congratulations for finishing the game! See you next time!")
        break
    # user_answer = fizz_buzz(int(input("Type in a value that is divisible "
    #                                   "by 3, 5 or 15: ")))
    # print(user_answer)

# for i in range(1, 101):
#     print(fizz_buzz(i))
