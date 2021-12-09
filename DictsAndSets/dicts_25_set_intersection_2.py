trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

trial_intersection = trial_1.intersection(trial_2)
print(trial_intersection)

print("-"*80)

rpg_video_games = {
    "Mass Effect",
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "The Witcher 3",
    "Dragon Age 2",
}

action_video_games = {
    "GTA 5",
    "Dragon Age 2",
    "Far Cry 3",
    "The Witcher 3",
    "Mass Effect",
    "Castlevania: Symphony of the Night",
    "Neverwinter Nights",
}

# Another set with video-games that are only for pc. I'm not sure if those
# games are indeed pc-only, but I believe it matters little for our purposes.
pc_only_video_games = {
    "Far Cry 3",
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "Baldur's Gate 2",
    "Fahrenheit: Indigo Prophecy",
    "The Witcher 3",
}

# Intersection of more than 2 sets using the intersection method:
video_games_intersection = rpg_video_games.intersection(action_video_games,
                                                        pc_only_video_games)
print(video_games_intersection)

# Intersection of more than 2 sets using the operator:
video_games_intersection_2 = rpg_video_games & action_video_games & \
                             pc_only_video_games
print(video_games_intersection_2)