class VideoGames(object):
    # We can add an attribute that all objects in VideoGames will share
    machine_to_play = "Computer"

    def __init__(self, name, time_to_complete):
        self.name = name
        self.time_to_complete = time_to_complete
        self.on = False

    def switch_on(self):
        self.on = True


call_warhammer = VideoGames("Call of Warhammer", 100)
nwn = VideoGames("Neverwinter Nights", 210.50)
nwn.price = 30

print(VideoGames.machine_to_play)
print(call_warhammer.machine_to_play)
print(nwn.machine_to_play)

print("-" * 60)

# Changing machine_to_play in the class:
VideoGames.machine_to_play = "Playstation 4"
print(VideoGames.machine_to_play)
print(call_warhammer.machine_to_play)
print(nwn.machine_to_play)

# Changing machine_to_play only in NWN. Doesn't affect the class as a whole
print("-" * 60)
nwn.machine_to_play = "XBox One"
print(VideoGames.machine_to_play)
print(call_warhammer.machine_to_play)
print(nwn.machine_to_play)


print(VideoGames.__dict__)
print(call_warhammer.__dict__) # Notice that in the output machine_to_play
# is not in call_warhammer or nwn because it belongs to the class and, thus,
# to both call_warhammer and nwn
print(nwn.__dict__)