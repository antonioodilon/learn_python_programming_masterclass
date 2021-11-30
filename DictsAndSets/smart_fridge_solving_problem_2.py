from smart_fridge_contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Adds required `items` and their respective `amounts` to `data` dict.
    :param data: dict
    :param item: str
    :param amount: int
    :return: None
    """
    data[item] = data.setdefault(item, 0) + amount
    
    # Does the same as this:
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount


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
                print(f"\tYou need {quantity_to_buy} of {food_item}. Go "
                      f"buy some groceries!")
                add_shopping_item(shopping_cart, food_item, quantity_to_buy)
        for things in shopping_cart.items():
            print(things)