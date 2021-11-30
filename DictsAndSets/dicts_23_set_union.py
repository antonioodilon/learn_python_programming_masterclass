rpg_video_games = {
    "Mass Effect",
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "Baldur's Gate 2",
    "The Witcher",
    "Dragon Age 2",
}
print(rpg_video_games)

action_video_games = {
    "GTA 5",
    "Dragon Age 2",
    "Far Cry 3",
    "The Witcher",
    "Mass Effect",
    "Castlevania",
}
print(action_video_games)

all_video_games = rpg_video_games.union(action_video_games)
print(all_video_games)

all_video_games_2 = action_video_games.union(rpg_video_games)
print(all_video_games_2)

# We'll see the difference between the union operator and the union method
# in the future
all_video_games_3 = action_video_games | rpg_video_games
print(all_video_games_3)