# Revisiting challenge2

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("Nested for loop:")
print("-" * 80)
for loc in sorted(locations):  # sorted(locations) returns a list containing all
    # the keys of locations in a sorted order
    # print(loc)
    exits_to_destination_1 = []
    for exit_option in exits:  # exit_option represents the key to the dict exits
        if loc in exits[exit_option].values():
            exits_to_destination_1.append((exit_option, locations[exit_option]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)

print("List comprehension inside a for loop")
print("-" * 80)
for loc in sorted(locations):
    exits_to_destination_2 = [(exit_option, locations[exit_option]) for exit_option
                              in exits if loc in exits[exit_option].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)

print("Nested comprehension")
print("-" * 80)

exits_to_destination_3 = [[(exit_option, locations[exit_option]) for exit_option
                           in exits if loc in exits[exit_option].values()]
                          for loc in sorted(locations)]
print(exits_to_destination_3)
# print("-" * 80)
# print(list_tuples for list_tuples in enumerate(exits_to_destination_3))
    # This produces the following output: <generator object <genexpr> at 0x00000249F12F5EE0>

print("-" * 80)

for list_tuples in exits_to_destination_3:
    print(list_tuples)

print("-" * 80)

for index, value in enumerate(exits_to_destination_3):
    print("Locations leading to {}".format(index), end="\t")
    print(value)
