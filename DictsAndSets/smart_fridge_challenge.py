from smart_fridge_contents import pantry, recipes

display_dict = {}
shopping_cart = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe:")
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"Your next meal will be: {selected_item}")
        ingredients_list = recipes[selected_item]
        print(f"Here's a list of ingredients for your next meal: "
              f"{ingredients_list}")

        for food_item, required_quantity in ingredients_list.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} is available!")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                shopping_cart[food_item] = quantity_to_buy
                print(f"\tYou need {quantity_to_buy} of {food_item}. Go "
                      f"buy some groceries!")
    print(f"Here is your shopping cart: {shopping_cart}")