available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "Stabilizer",
                   "HDMI Cable"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1 # Because the index of a list starts with 0
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
            print(computer_parts)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
            print(computer_parts)
    elif current_choice not in "01234567":
        print("Please choose one of the options below")
        for number, part in enumerate(available_parts):
            print("{0} : {1}".format(number + 1, part))
    elif current_choice == "0":
        break
    # enumerate() gets a pair of values: index position and name of the variable
    current_choice = input()
print("You have purchased the following items: {}".format(computer_parts))