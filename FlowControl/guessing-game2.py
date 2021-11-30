import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: remove after testing!
# Notice how useful a TO DO is!

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   #guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed correctly.")
    else:
        print("Your guess is wrong. Please try again.")
else:
    print("Congratulations! You got it the first time!")