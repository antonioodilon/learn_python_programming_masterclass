available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "Mouse mat",
                   "6": "Stabilizer",
                   "7": "HDMI Cable"
                   }
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"{chosen_part} is being added to your cart")
    else:
        print(f"Please add options from the list: {available_parts}")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("Press '0' to finish")
    current_choice = input("> ")