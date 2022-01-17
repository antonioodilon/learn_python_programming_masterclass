from generators_9_named_tuples_data import people, plants_dict, plants_list

if all([person[1] for person in people]):  # all() will return True if the
    # second item in the iterable person is filled. False otherwise.
    # all() is more interesting than iterating over all the items in a list
    print("Now sending email...")
else:
    print("User must insert email in the list of recipients")
# Another advantage of using any() and all() is that they don't iterate over
# all items. any() returns True as soon as a True value is found, and all()
# returns False as soon as a False value is found.

people_2 = []

if bool(people_2) and all([person[1] for person in people_2]):  # We need to
    # insert bool(people_2) here, because otherwise we will be sending an
    # email to an empty list. See generators_8_any_all_2 for clarification
    print("Now sending email...")
else:
    print("User must insert email in the list of recipients")
# Hence, ALWAYS TEST FOR EDGE CASES! Things like values equalling zero,
# empty lists, empty dicts or sets etc, values far greater than one would
# expect etc

# "Making sure that our code handles invalid data is difference between an
# OK program and a great one." -> Tim Buchalka's words in the lesson 393

# Now using any:
if any([plant.plant_type == "Shrub" for plant in plants_list]):
    print("This pack contains Shrub")
else:
    print("Shrub is missing from this pack")