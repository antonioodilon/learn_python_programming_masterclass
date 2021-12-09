# VERY IMPORTANT! If you write into a file that already exists, the existing
# file will be overwritten!

fantasy_characters = [
    "Gorion's Ward",
    "Viconia DeVir",
    "Alucard",
    "Belmont",
    "Valkia The Bloody",
]

with open("fantasy characters.txt", "w") as fantasy_file:
    for char in fantasy_characters:
        print(char, file=fantasy_file)
# Notice that a file called "fantasy characters.txt" has been created in our
# project file

more_characters = [
    "Shepard",
    "Yoshimo",
    "Nalia",
    "Aerie",
    "Imoen",
    "Thorgar the Blooded One",
]

with open("R:\\Antonio\\1_Coding\\more characters.txt", "w") as char_file:
    for char in more_characters:
        print(char, file=char_file)