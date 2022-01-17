import timeit

# The other way of using timeit is by enclosing our code in functions instead
# of transforming them into strings.

setup = """\t
gc.enable()
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
"""

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


# Inside the function we are going to make some changes. We need to get rid
# of the print statements in the function because they are relatively slow.
def nested_loop():
    result = []  # One change
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for exit_option in exits:
            if loc in exits[exit_option].values():
                exits_to_destination_1.append((exit_option, locations[exit_option]))
        result.append(exits_to_destination_1)  # Second change
    # print the result before returning:
    for x in result:
        pass
    return result  # Final change
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_1)


def loop_comprehension():
    result = [] # One change
    for loc in sorted(locations):
        exits_to_destination_2 = [(exit_option, locations[exit_option]) for exit_option
                                  in exits if loc in exits[exit_option].values()]
        result.append(exits_to_destination_2) # Second change
    # print the result before returning:
    for x in result:
        pass
    return result # Final change
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_2)


def nested_comp():
    exits_to_destination_3 = [[(exit_option, locations[exit_option]) for exit_option
                               in exits if loc in exits[exit_option].values()]
                              for loc in sorted(locations)]
    # print the result before returning:
    for x in exits_to_destination_3:
        pass
    return exits_to_destination_3  # In this function we only need one change
    # for index, value in enumerate(exits_to_destination_3):
    #     print("Locations leading to {}".format(index), end="\t")
    #     print(value)


# Transforming nested_comp() into a generator
def nested_gen():
    exits_to_destination_3 = ([(exit_option, locations[exit_option]) for exit_option
                               in exits if loc in exits[exit_option].values()]
                              for loc in sorted(locations))
    for x in exits_to_destination_3:
        pass
    return exits_to_destination_3


print(nested_loop())
print(loop_comprehension())
print(nested_comp())
print(nested_gen())
# This part here only works with functions that don't take any arguments:
result_1 = timeit.timeit(nested_loop, setup, number=1000)
result_2 = timeit.timeit(loop_comprehension, setup, number=1000)
result_3 = timeit.timeit(nested_comp, setup, number=1000)
result_4 = timeit.timeit(nested_comp, setup, number=1000)
# Now the results are a lot faster because we no longer need to do all that
# printing
print("Nested loop:\t{}".format(result_1))
print("Loop comprehension:\t{}".format(result_2))
print("Nested comprehension:\t{}".format(result_3))
print("Nested generator:\t{}".format(result_4))
# In conclusion, we can say that all three results are very very similar,
# and that unless performance is absolutely critical for the program, there
# doesn't seem to be much of a reason to choose one approach rather than
# the other as far as performance is concerned.

# In Tim's case the generator was a lot faster, but in my case it was just
# a little bit faster than the others. According to him the generator doesn't
# need to be spending time creating lists.