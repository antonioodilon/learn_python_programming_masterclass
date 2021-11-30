list_videogames = "Here's a list of video games you can play:\n" \
                  "1)\t Baldur's Gate\n" \
                  "2)\t Baldur's Gate II\n" \
                  "3)\t Neverwinter Nights\n" \
                  "4)\t Neverwinter Nights II\n" \
                  "5)\t Temple of Elemental Evil\n" \
                  "6)\t Fallout\n" \
                  "7)\t Fallout II\n" \
                  "8)\t Icewind Dale\n" \
                  "9)\t Icewind Dale II\n" \
                  "10)\t Arcanum: Of Steamworks and Magick Obscura\n" \
                  "11)\t Planescape: Torment\n" \
                  "0)\t None"

print(list_videogames)

while True:
    print()
    user_choice = int(input("Choose a game of your preference: press a number "
                            "from 1 to 11, or press 0 if you don't feel like "
                            "playing any games now. "))
    if 0 < user_choice <= 11:
        print()
        print("Game number {} is a great choice! "
              .format(user_choice))
    elif user_choice >= 12:
        print()
        print("Please choose a game from one of the available games in "
              "the list. {} ".format(list_videogames))
    elif user_choice == 0:
        print()
        print("You haven't chosen any games, and have gone studying Math "
              "or Python instead.")
        break

'''
user_choice = int(input("Choose a game of your preference: press a number "
                        "from 1 to 11, or press 0 if you don't feel like "
                        "playing any games now. "))
'''

'''
while True:
    user_choice = int(input("Choose a game of your preference: press a number "
                            "from 1 to 11, or press 0 if you don't feel like "
                            "playing any games now. "))
    if 0 < user_choice <= 11:
        input("Game number {} is a great choice! Now choose another one: "
              .format(user_choice))
    elif user_choice >= 12:
        input("Please choose a game from one of the available games in "
              "the list: {} ".format(list_videogames))
    elif user_choice == 0:
        print("You haven't chosen any games, and have gone studying Math "
              "or Python instead.")
        break
'''


'''
for i in range(0,12):
    if user_choice == i:
        print("Game number {} is a great choice!".format(user_choice))
    elif user_choice > 12:
        print("Please choose a game from one of the available games in"
              "the list")
    elif user_choice == 0:
        print("You haven't chosen any games, and have gone studyin Math"
              "or Python instead.")
        break
'''

'''
while user_choice >= 1:
    if user_choice >= 1:
        print("Game number {} is a great choice!".format(user_choice))
    elif user_choice > 12:
        print("Please choose a game from one of the available games in"
              "the list")
    else:
        print("You haven't chosen any games, and have gone studyin Math"
              "or Python instead.")
        break
'''