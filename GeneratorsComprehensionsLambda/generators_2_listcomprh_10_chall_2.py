# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.


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

# My solution to the first part of this challenge:
list_exits = [value for key, value in locations.items() if key == 1 or key == 2]
print(list_exits)

print("-" * 80)

# My solution to the second part of the challenge:
list_exits_2 = [(key, value) for key, value in locations.items() if key == 1 or key == 2]
# (key, value) is now a tuple
print(list_exits_2)

print("-" * 80)

# My solution to the third part of the challenge:
for key_exits, value_exits in exits.items():
    list_exits_3 = [(key, value, value_exits) for key, value in locations.items()
                    if key == key_exits]
    print(list_exits_3)

print("-" * 80)

for key_locations, value_locations in locations.items():
    for key_exits, value_exits in exits.items():
        if key_locations == key_exits:
            print(value_locations, " : ", value_exits)


'''
Previous attempts below:
'''
        # for key_value, value_value in value_exits.items():
        #     if key_locations == key_exits:
        #         print(value_locations, " : ", value_exits)
            # print(key_exits, " : ", key_value, value_value)

# for key_exits, value_exits in exits.items():
#     for key, value in locations.items():
#         if key_exits == key:
#             print()
    # list_exits_2 = [(key, value) for key, value in locations.items() if key == 1 or key == 2]


# list_exits_2 = [an_exit for an_exit in list_exits]
# print(list_exits_2)
#
# print("-" * 80)
#
# for item in list_exits_2:
#     # for char in item:
#     "".join(item)
#     # print(char)
#     print(item)
#     # list_exits_3 = ["".join(char) for char in item]
    # print(list_exits_3)
# for an_exit in list_exits:
#     tuple(an_exit)
#
#     print(an_exit)

# for key, value in locations.items():
#     list_exits_2 = [value for value in locations.values() if key == 1 or key == 2]
#     list_exits_2 = [value in locations.values() if key == 1 or key == 2 else "skipped"]
#     print(list_exits_2)

# Previous attempts below:
# for key, value in locations.items():
# list_exits = [value if key == 1 or key == 2 else "skipped" for key, value in locations.items()]
# list_exits = [value if key == 1 or key == 2 else value for key, value in locations.items()]
# print(list_exits)

# for key, value in locations.items():
#     list_exits_2 = [value for value in locations.values() if key == 1 or key == 2]
#     # list_exists_2 = [value if key == 1 or key == 2 for value in locations.values()]
#     print(list_exits_2)
# print(locations.values())