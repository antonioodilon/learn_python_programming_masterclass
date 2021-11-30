songs = [("Dead Sun", "British Murder Boys", 2011),
          ("Latin Lovers", "Monika Kruse", 2008),
          ("Bis Zum Nachsten Tag", "Schwefelgelb", 2016),
          ("Tunox", "Chris Liebing", 1992),
          ("Sambassim", "Fernanda Porto", 2010),
          ]

print(len(songs))

for song in songs:
    name, artist, year = song
    print("Song: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
# song, not songs, because we want to target each song's information

print("-"*60)

# A more efficient code, even though the previous one can also be useful:
for name, artist, year in songs:
    print("Song: {}, Artist: {}, Year: {}"
          .format(name, artist, year))