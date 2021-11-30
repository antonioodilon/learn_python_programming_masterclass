available_parts = {"1": "Computer",
                   "2": "Monitor",
                   "3": "Keyboard",
                   "4": "Mouse",
                   "5": "Mouse mat",
                   "6": "Stabilizer",
                   "7": "HDMI Cable"
                   }
shopping_cart = {}
current_choice = input("Please choose a computer part to add to your cart: ")

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in shopping_cart:
            print(f"Removing {chosen_part} from the dictionary.")
            shopping_cart.pop(current_choice)  # current_choice, not
            # chosen_part, because it was current_choice that was added
            # to shopping_cart, not chosen_part
        else:
            print(f"{chosen_part} is being added to your cart")
            shopping_cart[current_choice] = chosen_part
        print("This is your current shopping cart: {}".format(shopping_cart))
        current_choice = input("Please choose another computer part to add "
                               "to your cart: ")
    else:
        print("Please choose one of the available items below: ")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("Or press '0' to terminate.")
        current_choice = input()