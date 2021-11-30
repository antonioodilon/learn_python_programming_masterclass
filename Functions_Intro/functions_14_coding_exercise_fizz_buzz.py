# count = 0


# Better solution:
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


for i in range(0, 101):
    print(fizz_buzz(i))

# First attempt:
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 15 != 0:
#         print("The number is {}. Fizz!".format(i))
#     elif number % 5 == 0 and number % 15 != 0:
#         print("The number is {}. Buzz!".format(i))
#     elif number % 15 == 0:
#         print("The number is {}. Fizz buzz!".format(i))
#
#
# for i in range(0, 101):
#     print(fizz_buzz(i))

# program_start = fizz_buzz()


# A different program:
# def fizz_buzz_2(user_answer):
#     for i in range(1, 101):
#         user_answer = int(input("Please pick a number between 1 and 100: "))
#         if user_answer not in range(1, 101):
#             print("You must pick a number between 1 and 100.")
#             continue
#         elif user_answer % 3 == 0 and user_answer % 15 != 0:
#             print("The number is {}. Fizz!".format(user_answer))
#         elif user_answer % 5 == 0 and user_answer % 15 != 0:
#             print("The number is {}. Buzz!".format(user_answer))
#         elif user_answer % 15 == 0:
#             print("The number is {}. Fizz buzz!".format(user_answer))
#         else:
#             print("Please try again.")
#
#
# answer = fizz_buzz_2(2)
