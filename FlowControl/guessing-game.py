answer = 5
print("Please guess a number between 1 and 10: ")
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


'''
if guess < answer:
    print("Please guess higher.")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed correctly.")
    else:
        print("Your guess is wrong. Please try again.")
elif guess > answer:
    print("Please guess lower.")
    guess = int(input())
    if guess == answer:
        print("Well done, you have guessed correctly.")
    else:
        print("Your guess is wrong. Please try again.")
else:
    print("Congratulations! You got it the first time!")
'''