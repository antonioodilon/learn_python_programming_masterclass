import shelve

rpg_videogames_2 = shelve.open("rpg_videogames_4")
rpg_videogames_2["Baldur's Gate"] = "The story of the Bhaalspawn"
rpg_videogames_2["Planescape Torment"] = "Set in another D&D universe"
rpg_videogames_2["Neverwinter Nights"] = "The Jewel of the North suffers " \
                                         "from 'The Wailing Death'"
rpg_videogames_2["Icewind Dale"] = "Another RPG coded using the Infinity " \
                                   "Engine"
rpg_videogames_2["Dragon Age: Origins"] = "From this shelve, it's the only " \
                                          "one not based on D&D"

# We can also iterate through the shelve:
while True:
    game = input("Please enter a game you would like to play: ")
    if game in rpg_videogames_2:
        description = rpg_videogames_2.get(game, "This game is not available")
        # We can use the .get() method, just like a dictionary
        print(description)
        # print(rpg_videogames_2[game], "This game is not available")
    elif game == "quit":
        print("Goodbye! Time to study now, right?")
        break

print("-" * 80)

ordered_games = list(rpg_videogames_2.keys())
ordered_games.sort()

for game in ordered_games:
    print(f"{game}: {rpg_videogames_2[game]}")

# print(ordered_games)

rpg_videogames_2.close()  # Closing the shelve manually