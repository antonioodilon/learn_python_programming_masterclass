import shelve

rpg_videogames_2 = shelve.open("rpg_videogames_5")
rpg_videogames_2["Baldur's Gate"] = "The story of the Bhaalspawn"
rpg_videogames_2["Planescape Torment"] = "Set in another D&D universe"
rpg_videogames_2["Neverwinter Nights"] = "The Jewel of the North suffers " \
                                         "from 'The Wailing Death'"
rpg_videogames_2["Icewind Dale"] = "Another RPG coded using the Infinity " \
                                   "Engine"
rpg_videogames_2["Dragon Age: Origins"] = "From this shelve, it's the only " \
                                          "one not based on D&D"

for key in rpg_videogames_2.keys():
    print(key)
print(rpg_videogames_2.keys())  # Notice in the output that you can only
# view it, not change it. "KeysView(<shelve.DbfilenameShelf etc..."

print("-" * 80)

for value in rpg_videogames_2.values():
    print(value)
print(rpg_videogames_2.values()) # Notice in the output that you can only
# view it, not change it. "ValuesView(<shelve.DbfilenameShelf etc..."

rpg_videogames_2.close()