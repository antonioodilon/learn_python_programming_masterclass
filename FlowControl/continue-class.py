shopping_list = ["ground beef", "eggs", "butter", "milk", "chicken breast", "bacon"]
updated_shopping_list = []

for item in shopping_list:
    if item != "milk":
        updated_shopping_list.append(item)

print(updated_shopping_list)

print("-" * 80)

for item in shopping_list:
    if item != "milk":
        print("You must buy {}".format(item))

print("-" * 80)

for item in shopping_list:
    if item == "milk":
        continue
        #Continue causes all the remaining code in the block to be skipped, so it will go back to the for statement!
    print("You must buy {}".format(item))