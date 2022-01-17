from generators_9_named_tuples_data import people, plants_dict, plants_list

# print(plants_dict)

# for key, value in plants_dict.items():
#     print(key, value)
    # for val in value:
    #     print(key, value, val)

if any({value.plant_type == "Grass" for plant, value in plants_dict.items()}):
    print("Found a plant of type 'Grass'")
else:
    print("Plant of type 'Grass' wasn't found")

print("-" * 60)

if any({value.plant_type == "Cactus" for plant, value in plants_dict.items()}):
    print("Found a plant of type 'Cactus'")
else:
    print("Plant of type 'Cactus' wasn't found")

print("-" * 60)

if any({value for key, value in plants_dict.items() if "Flower" in value}):
    print("Found a plant of type 'Flower' - using a different method")
else:
    print("Plant of type 'Flower' wasn't found - using a different method")

print("-" * 60)

if any({value for key, value in plants_dict.items() if "Cactus" in value}):
    print("Found a plant of type 'Cactus' - using a different method")
else:
    print("Plant of type 'Cactus' wasn't found - using a different method")

print("-" * 60)

# In Tim's solution he iterated only through the values of the dict. Remember
# that the .values() function for a dict doesn't iterate through the keys and
# values - just through the values!
if any({value for value in plants_dict.values() if "Flower" in value}):
    print("Found a plant of type 'Flower' - using another approach")
else:
    print("Plant of type 'Flower' wasn't found - using another approach")

print("-" * 60)

# Don't forget to insert .plant_type!
if any({value.plant_type == "Flower" for value in plants_dict.values()}):
    print("Found a plant of type 'Flower' - using another approach")
else:
    print("Plant of type 'Flower' wasn't found - using another approach")

print("-" * 60)

if any({plants_dict[key].plant_type == "Flower" for key in plants_dict}):
    print("Found a plant of type 'Flower' - using a fourth approach")
else:
    print("Plant of type 'Flower' wasn't found - using a fourth approach")