import shelve

with shelve.open("rpg_videogames_3") as rpg_videogames:
    rpg_videogames["Baldur's Gate"] = "The story of the Bhaalspawn"
    rpg_videogames["Planescape Torment"] = "Set in another D&D universe"
    rpg_videogames["Neverwinter Nights"] = "The Jewel of the North suffers " \
                                           "from 'The Wailing Death'"
    rpg_videogames["Icewind Dale"] = "Another RPG coded using the Infinity " \
                                      "Engine"
    rpg_videogames["Dragon Age: Origins"] = "From this shelve, it's the only " \
                                            "one not based on D&D"

    print(rpg_videogames["Baldur's Gate"])
    print(rpg_videogames["Neverwinter Nights"])

    rpg_videogames["Neverwinter Nights"] = "The game I am playing at the " \
                                           "moment"
    # We've changed the value of "Neverwinter Nights"

    print("-" * 80)

    for game in rpg_videogames:
        print(f"{game}: {rpg_videogames[game]}")