# See the code buy_computer_parts in section "Sequences"

# Below is also my solution to Tim Buchalka's Dictionary Menu Challenge
# (lesson 186, Section 7)

available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "Mouse mat",
                   "6": "Stabilizer",
                   "7": "HDMI Cable"
                   }
shopping_cart = []
current_choice = input("Please choose a computer part to add to your cart: ")

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"{chosen_part} is being added to your cart")
        shopping_cart.append(chosen_part)
        print("This is your current shopping cart: {}".format(shopping_cart))
        current_choice = input("Please choose another computer part to add "
                               "to your cart: ")
    elif current_choice not in available_parts:
        print("Please choose one of the available items below: ")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("Or press '0' to terminate.")
        current_choice = input()
    # elif current_choice == '0':
    #     print("Terminating the program now. Here is your shopping cart:"
    #           " {}".format(shopping_cart))
    #     break  # TODO: Improve this!
