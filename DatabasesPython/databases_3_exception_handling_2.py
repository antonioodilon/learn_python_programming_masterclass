import sys


# This is the function Tim wrote. I decided to use it here in order to see
# how else works in a try and except block
def division_numbers(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        # except Exception:
        #     print("Invalid input entered. Please try again")
        # We could invoke the superclass Exception here to handle all exceptions,
        # but it is almost always a good idea to handle each specific exception
        # appropriately.
        except (MemoryError, OverflowError):
            print("The program cannot handle numbers this big.")
        except ValueError:
            print("Invalid number entered. Please try again.")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes, no matter what")


first_number = division_numbers("Please enter the first number ")
second_number = division_numbers("Please enter the second number ")

try:
    print("{} divided by {} is {}"
          .format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Please type in a divisor different from zero.")
    sys.exit(2)
else:
    print("Division performed successfully!")
    # Unlike what one might expect, in a try and except block, else only
    # works if the try block was executed successfully. except works if and
    # only if try wasn't executed.