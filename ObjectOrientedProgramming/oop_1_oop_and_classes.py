# From Tim's description of OOP, it seems that it is very useful in robotics.
# A class is a template for creating objects. Any objects created inside
# the class will have the same characteristics.

a = 12
b = 13
print(a + b)  # Everything in Python is an object, even the + sign. If you hold
# ctrl + press the + sign, it will go to the same method as __add__()
print(a.__add__(b))

print("-" * 60)

# Creating a class called VideoGames and its objects:


class VideoGames(object):  # Use camelcase when defining classes
    # object is a name for an instance of a class

    def __init__(self, name, time_to_complete):
        self.name = name
        self.time_to_complete = time_to_complete
        self.on = False  # self.on = False means that at the moment the game
        # hasn't been initialized


call_warhammer = VideoGames("Call of Warhammer", 100)
print(call_warhammer.name)
print(call_warhammer.time_to_complete)
print(call_warhammer.on)  # Returns false

call_warhammer.time_to_complete = 150
print(call_warhammer.time_to_complete)
call_warhammer.on = True  # Now call_warhammer has been turned on
print(call_warhammer.on)

nwn = VideoGames("Neverwinter Nights", 210.50)

print("-" * 60)

print("{0} takes {1} hours to complete.\n{2} takes {3} hours to complete."
      .format(call_warhammer.name, call_warhammer.time_to_complete,
              nwn.name, nwn.time_to_complete))

# Because call_warhammer and nwn are objects, we can specify their attributes
# in the replacement fields:
print("{0.name} takes {0.time_to_complete} hours to complete.\n{1.name} takes"
      " {1.time_to_complete} hours to complete.".format(call_warhammer, nwn))







