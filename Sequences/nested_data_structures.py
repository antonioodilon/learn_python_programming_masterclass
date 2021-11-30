albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for album, artist, year, songs in albums:
    print("Album: {0}, Artist: {1}, Year: {2}, Song list: {3}"
          .format(album, artist, year, songs))

# Printing "Mayhem" in "More Mayhem"
print(albums[3][3][2][1])

print()

#Or doing it the longer way:

more_mayhem = albums[3]
print(more_mayhem)

print()

mayhem_songs = more_mayhem[3]
print(mayhem_songs)

print()

mayhem = mayhem_songs[2]
print(mayhem)

print()

mayhem_title = mayhem[1]
print(mayhem_title)

print()

#Exercise solution:
print(albums[1][3][5][1])
print(albums[2][2])
print(albums[3][3][3][0])
print(albums[2][3][1])