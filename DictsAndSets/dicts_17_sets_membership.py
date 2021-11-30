# Revisiting the code that was the summary challenge for the FlowControl
# section. The code I came up with is called challenge-flow-control;
# however, I am using Tim Buchalka's code, found in the resources section
# of the video.

# Sets can also have the range function. For example, test this code in the
# Python Console: set(range(0, 20, 2))

choice = "-"  # initialise choice to something invalid

    # if choice in "12345": -> Old code!
    # if choice in list("12345"): -> One solution is a list, but a set is better
    # Another option: if choice in set("12345"):
while choice != "0":
    if choice in {"1", "2", "3", "4", "5"}:
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

# Using a set in this program is faster than a list because a set uses
# hash code (like a key in a dictionary)

# Using a set literal in this case {"1", "2", "3", "4", "5"} instead of
# a set() function is faster, more performative, because in the latter
# case Python has to recreate the set each time around the loop