# This is a list, not a set:
rpg_video_games = [
    "Mass Effect",
    "Baldur's Gate",
    "Neverwinter Nights",
    "Icewind Dale",
    "Baldur's Gate 2",
    "The Witcher",
    "Dragon Age 2",
]

# This is a list, not a set:
action_video_games = [
    "GTA 5",
    "Dragon Age 2",
    "Far Cry 3",
    "The Witcher",
    "Mass Effect",
    "Castlevania",
]

sym_diff_video_games = set(rpg_video_games) ^ set(action_video_games)
print(sym_diff_video_games)

# The method is good because we can check the symmetric difference between
# a set and any iterable (a list, in this case)
sym_diff_video_games = set(rpg_video_games).symmetric_difference\
    (action_video_games)
print(sym_diff_video_games)

# Symmetric difference is commutative. Different from difference. So we
# can write it as:
sym_diff_video_games = set(action_video_games).symmetric_difference\
    (rpg_video_games)
print(sym_diff_video_games)

# symmetric_difference_update:
morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

print(set(morning).symmetric_difference_update(afternoon))