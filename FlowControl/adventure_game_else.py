available_exits = "Athkatla", "Wild Forest", "Dragonspear",\
                  "Baldur's Gate"
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an exit: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
else:
    print("Congratulations for completing the {} dungeon!".
          format(chosen_exit))
# Now else is related to the while loop