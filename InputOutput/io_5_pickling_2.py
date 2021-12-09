# We can even add more things to our pickle.imelda file
# Let's create a new file

import pickle

imelda = (
    "More Mayhem",
    "Imelda May",
    "2011",
    ((1, "Pulling the Rug"),
     (2, "Psycho"),
     (3, "Mayhem"),
     (4, "Kentish Town Waltz"),),
)

even = list(range(0, 22, 2))
odd = list(range(1, 23, 2))

with open("pickle.imelda_2", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(367, pickle_file, protocol=0)
# Because of protocol=0, the pickle.imelda_2 file is a lot more readable

# When we are loading the binary files so that they can be read, Python
# apparently reads it from top to bottom
with open("pickle.imelda_2", "rb") as imelda_file:
    imelda2 = pickle.load(imelda_file)
    even_list = pickle.load(imelda_file)
    odd_list = pickle.load(imelda_file)
    x = pickle.load(imelda_file)
# For security reasons, you should only unpickle data from sources you
# can trust

print(imelda2)

print("-" * 40)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)

print("-" * 40)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print("-" * 40)

for i in even_list:
    print(i)

print("-" * 40)

for j in odd_list:
    print(j)

print("-" * 40)

print(x)