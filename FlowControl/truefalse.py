day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go to the beach")
#The code (day == "Saturday" and temperature > 27) is treated as one thing, like a multiplication or division of two
#numbers in Math. We don't need the parentheses, but it makes our intentions clearer. day == "Saturday" is false
#and temperature > 27 is true, so this first part of the code is false. But since not raining evaluates to True
#(since it in fact isn't raining) and we have an "or", then it prints "Go to the beach"
else:
    print("Play Baldur's Gate")