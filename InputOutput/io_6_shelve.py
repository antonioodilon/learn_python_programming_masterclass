import shelve
# A shelve is similar to a dictionary, but one of the differences is that
# the keys can only be strings

with shelve.open("rpg_videogames") as rpg_videogames:
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
    # When you the key/value pairs in a shelve, you have to do so in the
    # same indentation as the code you used to create/open the shelve

print(rpg_videogames)  # From the output it is possible to confirm that
# rpg_videogames is indeed a shelve, and not a dictionary.

# Python saves the file as .db, which stands for DataBase. Can save in other
# formats as well


# Using a with statement, Python closes the shelve automatically after the
# with statement finishes.
# In the example below we will close it manually:
rpg_videogames_2 = shelve.open("rpg_videogames_2")
rpg_videogames_2["Baldur's Gate"] = "The story of the Bhaalspawn"
rpg_videogames_2["Planescape Torment"] = "Set in another D&D universe"
rpg_videogames_2["Neverwinter Nights"] = "The Jewel of the North suffers " \
                                       "from 'The Wailing Death'"
rpg_videogames_2["Icewind Dale"] = "Another RPG coded using the Infinity " \
                                 "Engine"
rpg_videogames_2["Dragon Age: Origins"] = "From this shelve, it's the only " \
                                        "one not based on D&D"

print(rpg_videogames_2["Baldur's Gate"])
print(rpg_videogames_2["Neverwinter Nights"])

rpg_videogames_2.close()  # Closing the shelve manually

print(rpg_videogames_2)
