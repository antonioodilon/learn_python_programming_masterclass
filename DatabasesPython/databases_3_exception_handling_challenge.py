# Write a program to ask the user to type two integers, and then return the
# result of one divided by the second. The program shouldn't crash, no matter
# what.

# def division_numbers():
#     x = int(input("Please type in the dividend "))
#     z = int(input("Please type in the divisor "))
#     try:
#         return x / z
#     except ZeroDivisionError:
#         while True:
#             print("Please type in a divisor different from zero.")
#             break
#     except (MemoryError, OverflowError):
#         print("The program cannot handle numbers this big.")
import sys


def division_numbers():
    while True:
        x = int(input("Please type in the dividend "))
        z = int(input("Please type in the divisor "))
        try:
            return x / z  # A return statement breaks out of the loop! Great!
            # print(x / z)
            # break
        except ZeroDivisionError:
            # while True:
            print("Please type in a divisor different from zero.")
        except (MemoryError, OverflowError):
            print("The program cannot handle numbers this big.")
        except ValueError:
            print("Invalid number entered. Please try again.")
        except EOFError:
            sys.exit(1)
            # Code inserted by Buchalka to handle end-of-file condition error

        # try:
        #     y = x / z
        #     if y == y:
        #         return y  # I wanted a return statement instead of a print
        #     # statement and couldn't figure out how to add the break code
        #     # after return. So I came up with this. However, I believe
        #     # there is a better way of writing this.
        #     else:
        #         break


print(division_numbers())
# print(division_numbers(2, 4))