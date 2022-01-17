from generators_9_named_tuples_data import basic_plants_list, plants_list

print(plants_list[0])

print("=" * 60)

for plant in basic_plants_list:
    print(plant[0])
    # Printing the first index value for each item in basic_plants_list.
    # The output is Andromeda, Bellflower, China Pink etc

print("=" * 60)

for plant in plants_list:
    print("{0} : {1}".format(plant.name, plant.scientific_name))
    # We can use dot notation, as if it were a class

print("=" * 60)

# Tuples are immutable, but we can use ._replace as a way to change the name(s)
# of a named tuple
example = plants_list[2]
print(example)
example = example._replace(plant_type='Tree')
print(example)

example_2 = plants_list[7]._replace(lifecycle='Eternal')
print(example_2)