from dicts_21_remove_method import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch |= interaction  # This is augmented assignment. Another
    #way to update a set
    # meds_to_watch.update(interaction)

    # Produces the same output as the one in dicts_23_set_union_2, but more
    # efficient because the union() method creates a new set each time around
    # the loop

print(sorted(meds_to_watch))

# Try with different sets, maybe the video games from previous codes, and
# creating sets with different companies, videogame genres. Or maybe films.