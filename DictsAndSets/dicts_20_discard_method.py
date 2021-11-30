travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print(items)

print("-"*80)

print("Please choose the way you want to travel: ")
for key, value in travel_mode.items():
    print(f"{key}: {value}")

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    print("You are carrying restricted items. We are removing them for you.")
    for restricted_items in restricted_items:
        items.discard(restricted_items)
        # items.remove(restricted_items)  # Remove raises an error, and in this
        # case it is not a good option

print("-"*80)

print("You need to pack: ")
for item in sorted(items):
    print(item)