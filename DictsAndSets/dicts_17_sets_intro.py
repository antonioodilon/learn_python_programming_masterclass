# Because sets are unordered, the items will always appear in random order
# whenever they are printed
# Items in the sets must be hashable. We can't put lists in sets, for example

video_games = {
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "Call of Warhammer",
    "Tsardoms Total War",
    "Baldur's Gate 2",
}
print(video_games)

for video_game in video_games:
    print(video_game)

print("-" * 60)

print("Indexing a sequence")
games_list = [
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "Call of Warhammer",
    "Tsardoms Total War",
    "Baldur's Gate 2",
]
print(games_list)
icewind_dale = games_list[2]
print(icewind_dale)

# print("Indexing a set is not possible")
# icewind_dale = video_games[2]   # See that we already get an error here
# print(icewind_dale)     # TypeError: 'set' object is not subscriptable

print("-" * 60)

# Since order isn't important in a set (it's the items that count), video_games
# and more_games should evaluate to true.
# For two lists to be evaluated to true, they need to contain the same items,
# in the same order.
more_games = {
    "Baldur's Gate 2",
    "Icewind Dale",
    "Baldur's Gate",
    "Tsardoms Total War",
    "Neverwinter Nights",
    "Call of Warhammer",
}

if video_games == more_games:
    print("Both sets are equal")
else:
    print("Both sets are different")