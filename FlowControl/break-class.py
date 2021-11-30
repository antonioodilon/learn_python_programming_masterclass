shopping_list = ["ground beef", "eggs", "butter", "milk", "chicken breast", "bacon"]

for item in shopping_list:
    if item == "milk":
        break
        #Break causes the for loop to terminate before being completed
    print("You must buy {}".format(item))

print("-" * 80)

item_to_find = "milk"
found_item = None
#None is when something has no value

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_item = index
        break
#Break is very useful when searching for specific items
#There is no point in continuing a search if the item has been found.
print("The item was found at the position {}".format(found_item))