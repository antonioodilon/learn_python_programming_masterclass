# Creating an algorithm to make the computer guess a number. See guessing-game files for reference.
low = 1
high = 1000

print("Please guess a number between {0} and {1}".format(low, high))
input("Press ENTER to start")

# More about while True: https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python
guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? Type h, l or c if the answer is correct "
          .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
        # Guess higher. The low end becomes 1 greater than the guess. For example, if the computer guessed 600
        # in a 1 to 1000 range but the answer is 700, then the range is now 601 to 1000.
        # pass # pass doesn't do anything. It's just a placeholder for the real code to be inserted later.
    elif high_low == "l":
        high = guess - 1
        # Guess lower. The high end becomes 1 smaller than the guess. For example, if the computer guessed 600
        # in a 1 to 1000 range but the answer is 500, then the range is now 1 to 599.
        # pass # pass doesn't do anything. It's just a placeholder for the real code to be inserted later.
    elif high_low == "c":
        print("I got the correct answer in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    #guesses = guesses + 1
    guesses += 1
