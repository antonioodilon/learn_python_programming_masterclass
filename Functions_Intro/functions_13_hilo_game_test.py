# Putting the code into functions makes testing easier!

LOW = 1
HIGH = 65535 # Test with different powers of 2. 2 to the power of 16 is 65536
# LOW and HIGH are now constants

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


# Avoid using the same name for your function parameters as the ones you
# create in your main code! For example, low and high variables being
# created on the top, and then parameters with the same names being
# created inside the function
def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guesses without being told {0} times. Max {1} guesses."
      .format(correct_count, max_guesses))
# Checking the maximum number of guesses