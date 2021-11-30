available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "Stabilizer",
                   "HDMI Cable"
                   ]
current_choice = "-"
computer_parts = []

while current_choice != 0:
    if current_choice in "1234567":
        print("Adding {} to the shopping cart".format(current_choice))
        if current_choice == "1":
            computer_parts.append("Computer")
        elif current_choice == "2":
            computer_parts.append("Monitor")
        elif current_choice == "3":
            computer_parts.append("Keyboard")
        elif current_choice == "4":
            computer_parts.append("Mouse")
        elif current_choice == "5":
            computer_parts.append("Mouse mat")
        elif current_choice == "6":
            computer_parts.append("Stabilizer")
        elif current_choice == "7":
            computer_parts.append("HDMI Cable")
    elif current_choice not in "01234567":
        print("Please choose one of the options below")
        for number, part in enumerate(available_parts):
            print("{0} : {1}".format(number + 1, part))
    elif current_choice == "0":
        break
# enumerate() gets a pair of values: index position and name of the variable
    current_choice = input()
print(computer_parts)

'''
    else:
        print("Please choose one of the options below")
        for part in available_parts:
            print("{0} : {1}".format(available_parts.index(part) + 1, part))
    current_choice = input()
    # elif current_choice == 0:
    # break
'''