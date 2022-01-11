# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.
#
# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimetres to 1 inch.

inch_measurement = (3, 8, 20)

cm_measurement = ['<enter your list comprehension here>']
cm_measurement_2 = [x * 2.54 for x in inch_measurement]

for x in inch_measurement:
    x *= 2.54
    cm_measurement.append(x)

print("Using a regular for loop: ", cm_measurement)
print("Using a list comprehension: ", cm_measurement_2)

# Once you've got the correct values, change the code to produce a tuple, rather than a list.
cm_measurement_tuple = tuple([x * 2.54 for x in inch_measurement])
# One way to output a tuple in a list comprehension

cm_measurement_tuple_2 = *(x * 2.54 for x in inch_measurement),
# Another way to output a tuple. Seen it here: https://www.pythonpool.com/tuple-comprehension/
# Notice the comma in the end!!

# Observation: using the augmented assignment *= didn't work here. Interestingly,
# it had to be used in the regular for loop, but in the list comprehension
# a regular * already did the trick.

print("Is the output a tuple? {0} : {1} ".format(type(cm_measurement_tuple),
                                                 cm_measurement_tuple))
print("Is the output a tuple? {0} : {1} ".format(type(cm_measurement_tuple_2),
                                                 cm_measurement_tuple_2))