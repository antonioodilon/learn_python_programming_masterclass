# Challenge 3: convert all the comprehensions in the previous challenges to
# for loops:

# From Challenge 1:
fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz"
            if x % 5 == 0 else str(x) for x in range(1, 51)]
# It's better if all the items in the list are strings. Hence the str(x)
print(fizzbuzz)

print("----Converting challenge 1 to a regular for loop:----")

fizzbuzz_list = []
for x in range(1, 51):
    if x % 15 == 0:
        fizzbuzz_list.append("fizz buzz")
    elif x % 3 == 0:
        fizzbuzz_list.append("fizz")
    elif x % 5 == 0:
        fizzbuzz_list.append("buzz")
    else:
        fizzbuzz_list.append(str(x))

print(fizzbuzz_list)

print()
print("----End of Challenge 1----")
print()

# From Challenge 2:
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

# Challenge 2 - Part 1
list_exits = [value for key, value in locations.items() if key == 1 or key == 2]
print(list_exits)

print("----Converting challenge 2 - Part 1 to a regular for loop:----")

list_exits_for_loop = []
for key_for_loop, value_for_loop in locations.items():
    if key_for_loop == 1 or key_for_loop == 2:
        list_exits_for_loop.append(value_for_loop)
print(list_exits_for_loop)

print()
print("----End of Challenge 2 - Part 1----")
print()

# Challenge 2 - Part 2
list_exits_2 = [(key, value) for key, value in locations.items() if key == 1 or key == 2]
print(list_exits_2)

print("----Converting challenge 2 - Part 2 to a regular for loop:----")

list_exits_for_loop_2 = []
for key_for_loop_2, value_for_loop_2 in locations.items():
    if key_for_loop_2 == 1 or key_for_loop_2 == 2:
        tuple_for_loop_2 = (key_for_loop_2, value_for_loop_2)
        list_exits_for_loop_2.append(tuple_for_loop_2)
print(list_exits_for_loop_2)

print()
print("----End of Challenge 2 - Part 2----")
print()

# Challenge 2 - Part 3
for key_exits, value_exits in exits.items():
    list_exits_3 = [(key, value, value_exits) for key, value in locations.items()
                    if key == key_exits]
    print(list_exits_3)

print("----Converting challenge 2 - Part 3 to a regular for loop:----")

list_exits_for_loop_3 = []
for key_exits_for_loop_3, value_exits_for_loop_3 in exits.items():
    for key_for_loop_3, value_for_loop_3 in locations.items():
        if key_for_loop_3 == key_exits_for_loop_3:
            tuple_for_loop_3 = (key_exits_for_loop_3, value_for_loop_3,
                                value_exits_for_loop_3)
            list_exits_for_loop_3.append(tuple_for_loop_3)

for item in list_exits_for_loop_3:
    print(item)


'''
Tim's solutions are below:
'''
# Challenge 2:
loc = 1
possible_exits = [locations[exit_f] for exit_f in exits if loc in exits[exit_f].values()]
print(possible_exits)

print("Now for a regular for loop:")

possible_exits_2 = []
for exit_f in exits:
    if loc in exits[exit_f].values():
        possible_exits_2.append(locations[exit_f])
print(possible_exits_2)

print()

loc = 1
possible_exits = [(exit_f, locations[exit_f]) for exit_f in exits if
                  loc in exits[exit_f].values()]
print(possible_exits)

print()

for loc in sorted(locations):
    possible_exits = [(exit_f, locations[exit_f]) for exit_f in exits if loc in
                      exits[exit_f].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(possible_exits)

print("Now for a regular for loop:")

for loc in sorted(locations):
    possible_exits_2 = []
    for exit_f in exits:
        if loc in exits[exit_f].values():
            possible_exits_2.append((exit_f, locations[exit_f]))
            # Two parentheses because the inner one is a tuple
    print("Locations leading to {}".format(loc), end='\t')
    print(possible_exits_2)