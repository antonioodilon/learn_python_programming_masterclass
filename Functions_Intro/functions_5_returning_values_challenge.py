import random


def get_integer(prompt):
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


highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    #
    # if guess == 0:
    #     break
    # if guess == answer:
    #     print("Well done, you guessed it")
    #     break
    # else:
    #     if answer > guess > 1:
    #         print("Please guess higher")
    #     elif highest < guess > answer:  # guess must be greater than answer
    #         print("Please guess lower")



# import random
#
#
# def get_integer(prompt):
#     temp = input(prompt)
#     while temp != answer:
#         if temp == 0:
#             break
#         # elif temp == answer:
#         #     print("Well done, you guessed it")
#         #     break
#         elif temp < answer:
#             print("Please guess higher")
#         elif temp > answer:  # guess must be greater than answer
#             print("Please guess lower")
#         if not temp.isnumeric():
#             print("Please type in a number")
#             # continue
#         else:
#             print("Please select a value from 1 to {}".format(highest))
#             continue
#     else:
#         if temp.isnumeric():
#             return int(temp)
#
#
# highest = 1000
# answer = random.randint(1, highest)
# print(answer)  # TODO: Remove after testing.
#   # initialise to any number that doesn't equal answer
# print("Please guess a number between 1 and {}: ".format(highest))
#
# guess = get_integer(int(": "))

# while guess != answer:
#     guess = get_integer(": ")
#
#     # if guess == 0:
#     #     break
#     if guess == answer:
#         print("Well done, you guessed it")
#         break
#     elif guess < answer:
#         print("Please guess higher")
#     elif guess > answer:  # guess must be greater than answer
#         print("Please guess lower")
