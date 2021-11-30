shopping_list = ["ground beef",
                 "eggs",
                 "chicken breast",
                 "beef liver",
                 "lard",
                 "bacon"]
print(shopping_list)
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["butter",
                  "coalho cheese"]
another_list = shopping_list
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

# Because lists are mutable, Python didn't need to create another object
# for this. Just modify the previous list.

a = b = c = d = e = another_list
print(a)
print("Adding chicken legs")
b.append("chicken legs")
print(c)
print(d)