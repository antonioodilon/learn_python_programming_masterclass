artist = "Album name", "Artist Name", "2021", (
    (1, "Song 1"),
    (2, "Song 2"),
    (3, "Song 3"),
    (4, "Song 4"),
)

print(artist)

with open("fictional musician.txt", "w") as fict_musician:
    for info in artist:
        print(info, file=fict_musician)
        # if info == tuple():
        #     for info2 in tuple():
        #         print(info2)
        # else:
        #     print(info, file=fict_musician)