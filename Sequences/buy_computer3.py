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
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    elif current_choice not in "01234567":
        print("Please choose one of the options below")
        for number, part in enumerate(available_parts):
            print("{0} : {1}".format(number + 1, part))
    elif current_choice == "0":
        break
    # enumerate() gets a pair of values: index position and name of the variable
    current_choice = input()
print(computer_parts)