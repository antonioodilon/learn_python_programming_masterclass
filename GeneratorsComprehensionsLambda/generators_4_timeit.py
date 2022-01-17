import timeit

# Copying the code from generators_3_nestcomprh_2.
# Using the timeit module, we are now going to compare which approach is more
# efficient

# Be aware that any other programs your computer is running, browsers, videos
# etc impact the performance of the computer, and thus the results that timeit
# produces

# It is very important also that we are comparing code that is doing the same
# thing.

# gc = garbage collection, and it is important, as our nested loop and our
# loop comprehension are constantly creating, throwing away and then recreating
# lists. Different from the nested comprehension, which creates a list once
# and iterates over it.
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

print("Approach #1:")
print("-" * 80)
# First thing to do is to transform everything into strings
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for exit_option in exits:
        if loc in exits[exit_option].values():
            exits_to_destination_1.append((exit_option, locations[exit_option]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
"""

print("Approach #2:")
print("-" * 80)
loop_comprehension = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(exit_option, locations[exit_option]) for exit_option
                              in exits if loc in exits[exit_option].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
"""

print("Approach #3:")
print("-" * 80)
nested_comp = """\
exits_to_destination_3 = [[(exit_option, locations[exit_option]) for exit_option
                           in exits if loc in exits[exit_option].values()]
                          for loc in sorted(locations)]
for index, value in enumerate(exits_to_destination_3):
    print("Locations leading to {}".format(index), end="\t")
    print(value)
"""

# Now let's see how long it takes for our code to execute:
# result_1 = timeit.timeit(nested_loop, globals=globals())

# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
# print("Nested loop:\t{}".format(result_1))

# We could leave the default parameter of number to 1 million, but that would
# take a lot of time to execute. But generally speaking, it is a good idea to
# not change the default parameter.

# Changing from globals=globals() to setup, as defined above
result_1 = timeit.timeit(nested_loop, setup, number=1000)
result_2 = timeit.timeit(loop_comprehension, setup, number=1000)
result_3 = timeit.timeit(nested_comp, setup, number=1000)
print("Nested loop:\t{}".format(result_1))
print("Loop comprehension:\t{}".format(result_2))
print("Nested comprehension:\t{}".format(result_3))
# Tim said that the comprehensions should be larger than the loops, but
# that is not the output I've been getting.


# result_2 = timeit.timeit(loop_comprehension, globals=globals(), number=1000)
# print("Loop comprehension:\t{}".format(result_2))
#
# result_3 = timeit.timeit(nested_comp, globals=globals(), number=1000)
# print("Nested comprehension:\t{}".format(result_3))