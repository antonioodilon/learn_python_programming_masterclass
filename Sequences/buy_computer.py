current_choice = "-"
computer_parts = [] # Create an empty list

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
    else:
        print("Please choose one of the options below:\n"
              "1) Computer\n"
              "2) Monitor\n"
              "3) Keyboard\n"
              "4) Mouse\n"
              "5) Mouse mat\n"
              "6) Stabilizer\n"
              "7) HDMI Cable\n"
              "0) To finish")
    current_choice = input()
    #elif current_choice == 0:
        #break

print(computer_parts)