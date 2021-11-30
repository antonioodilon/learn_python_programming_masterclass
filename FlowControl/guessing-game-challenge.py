import random

highest = 1000
answer = random.randint(1, highest)
print(answer) #TODO: remove after testing!
# Notice how useful a TO DO is!

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    '''number_of_guesses = 10
    number_of_guesses = number_of_guesses -= 1
    while number_of_guesses > 0:
        print("You have now {} guesses left.".format(number_of_guesses))
        if number_of_guesses == 0:
        print("Game over. You have run out of guesses.")
            break'''
    if guess == answer:
        print("You got it the first time! Congratulations!")
        break
    elif guess < answer:
        print("Please guess higher")
        print("(If you wish to terminate the program, please enter 0.)")
    else:   #guess must be greater than answer
        print("Please guess lower")
        print("(If you wish to terminate the program, please enter 0.)")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed correctly.")
        break
    elif guess == 0:
        print("Game over")
        break
else:
    print("Congratulations! You got it the first time!")