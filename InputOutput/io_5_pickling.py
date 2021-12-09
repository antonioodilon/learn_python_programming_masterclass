"""
“Pickling” is the process whereby a Python object hierarchy is converted into
a byte stream, and “unpickling” is the inverse operation, whereby a byte
stream (from a binary file or bytes-like object) is converted back into an
object hierarchy.
https://docs.python.org/3/library/pickle.html
"""

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

with open("pickle.imelda", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# Now we will load the data from the binary file using the .load() method
# in the pickle module
with open("pickle.imelda", "rb") as imelda_file:
    imelda2 = pickle.load(imelda_file)

print(imelda2)

album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

