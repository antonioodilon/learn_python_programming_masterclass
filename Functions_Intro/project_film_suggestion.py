# A project to suggest films to the user based on the user's preferences

# 1) Create a list of categories of films.
# 1.a) Each category of films is a list. -> DONE!
# 1.b) Each list contains a list  with the names of the films, the directors,
# and year -> DONE!
# 1.c) A list of genres with a list of films is better here because
# streaming apps are constantly changing their film catalogs -> DONE!

films_list = [["Action", [
    (1, "Film 1", "year"),
    (2, "Film 2", "year"),
    (3, "Film 3", "year"),
    (4, "Film 4", "year"),
    (5, "Film 5", "year"),
]],
              ["Comedy", [
                  (1, "Film 6", "year"),
                  (2, "Film 7", "year"),
                  (3, "Film 8", "year"),
                  (4, "Film 9", "year"),
                  (5, "Film 10", "year"),
              ]],
              ["Drama", [
                  (1, "Film 11", "year"),
                  (2, "Film 12", "year"),
                  (3, "Film 13", "year"),
                  (4, "Film 14", "year"),
                  (5, "Film 15", "year"),
              ]],
              ["Horror", [
                  (1, "Film 16", "year"),
                  (2, "Film 17", "year"),
                  (3, "Film 18", "year"),
                  (4, "Film 19", "year"),
                  (5, "Film 20", "year"),
              ]],
              ["Sci-fi", [
                  (1, "Film 21", "year"),
                  (2, "Film 22", "year"),
                  (3, "Film 23", "year"),
                  (4, "Film 24", "year"),
                  (5, "Film 25", "year"),
              ]],
              ]

# 2) Create an empty list that will be appended according to the choice of
# the user

user_list = []


# BLA = films_list[:][0:2]
# print(BLA)


# def suggest_films(user_choice):
print("Please choose a film of your preference. An invalid choice"
        "will ask you to choose a valid one again.")
for index, (genre, film_tuples) in enumerate(films_list):
    print("{0} : {1}".format(index + 1, genre))
    # user_choice = int(input())
# if 1 > user_choice > len(films_list):
#     print("Please insert a valid choice")
#     pass
# else:
#     print("Here is a list of available films in this genre: {}".format(films_list))
#         user_choice = input("Here is a list")


print("Hello! Welcome to Quality Films streaming service!")
continue_program = input("Press any button to continue")
user_input = int(input("Please choose a film of your preference. An "
                       "invalid choice will ask you to choose a valid "
                       "one again."))
# suggest_films(user_input)

# 3) Create a function that will make a choice for the user
# 3.a) The function will greet the user
# 3.b) Ask the user to choose a category of films of her/his preference.
# Print a list of genres
# 3.b1) Use a for loop here
# 3.b2) The user's input will be an integer
# 3.b3) If what the user types is not an available choice, go back to the
# start of the for loop
# 3.c) Print the list of films inside the chosen genre
# 3.c1) Ask the user how many films s/he would like the program to suggest
# 3.c2) While the number of items inside the empty list (step 2) is less
# than the user's choice:
# 3.c2a) Append the empty list with films according to the user's choice
# If the user inserts an invalid option, go back to the start of the loop
