class VideoGames(object):

    def __init__(self, name, time_to_complete):
        self.name = name
        self.time_to_complete = time_to_complete
        self.on = False

    def switch_on(self):
        self.on = True


call_warhammer = VideoGames("Call of Warhammer", 100)
nwn = VideoGames("Neverwinter Nights", 210.50)

print(call_warhammer.on)
# When we call the switch_on() method, self.on is set to True
call_warhammer.switch_on()
print(call_warhammer.on)

# Below is another way of switching the games on, this time by referencing
# the class
VideoGames.switch_on(nwn)  # Right here we need a parameter
print(nwn.on)
nwn.switch_on()  # Here we don't need a parameter
print(nwn.on)

print("-" * 80)

# We can provide an attribute to nwn
nwn.price = 30
print(nwn.price)
print(call_warhammer.price)  # When we do so, we don't do the same thing
# for call_warhammer. This line of code produces an error