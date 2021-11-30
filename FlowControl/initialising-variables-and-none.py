shopping_list = ["ground beef", "eggs", "butter", "milk", "chicken breast", "bacon"]

item_to_find = "eggs"
found_item = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_item = index
        break

#A better way to write this code:
#if item_to_find in shopping_list:
#    found_item = shopping_list.index(item_to_find)

if found_item is not None:
    print("The item was found at the position {}".format(found_item))
else:
    print("I'm sorry, but {} cannot be found".format(item_to_find))