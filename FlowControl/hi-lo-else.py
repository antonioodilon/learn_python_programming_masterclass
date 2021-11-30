low = 1
high = 1000

print("Please guess a number between {0} and {1}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Type h, l or c if the answer is correct "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got the correct answer in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    #guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}!".format(high))
    print("I got the answer in {} guesses.".format(guesses))
# The else statement is related to the while loop. Also, you can .format(high)
# or .format(low) because here high = low