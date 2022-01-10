import os
import fnmatch  # fnmatch compares a single file name against a value provided


# and returns True if it matches; returns False otherwise.


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdirectory = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdirectory):
                # We are not interested in the subdirectory path, so instead
                # of creating a variable with the name subdir_path, for example,
                # we just put an underscore _
                for album in albums:
                    yield os.path.join(album_path, album), album
                    # The os.path.join method concatenates various path components


def find_albums_2(root, artist_name):
    # Using a Generator Expression to deal with case for different Operating
    # Systems. Generator Expressions will be explained later in the course.
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
            # One Generator Expression solution that will work on Mac and Windows
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            # Another Generator Expression solution that will work on Mac, Windows and Linux
            subdirectory = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdirectory):
                for album in albums:
                    yield os.path.join(album_path, album), album


# When using the approach below, we can create a list of songs for any artist
# using just 4 lines of code, which is very good for performance:


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # We want the path, not the name
            # of the album
            yield song  # Both here and in the previous function we get the
            # list of songs and albums as we need them. More importantly,
            # they are not stored in memory. Because creating and destroying
            # lists will affect performance.


# Our generator returns a tuple containing the path to the directory and
# the name of the directory
album_list_zz = find_albums("music", "ZZ Top")
song_list_zz = find_songs(album_list_zz)
# We are chaining generators together by passing one generator as the argument
# to the next

# Returning all the songs whose artist_name has "Jim". We can do that with
# an asterisk. This is something that fnmatch.filter(directories, artist_name)
# (line 8) does. It's a feature of fnmatch
album_list_jim = find_albums_2("music", "jim*")  # IMPORTANT! Linux is case-sensitive
# for this, while Windows isn't, as long as you're using a hard drive that is
# # formatted with NTFS!
song_list_jim = find_songs(album_list_jim)

# Printing all the songs by ZZ Top:
for song_from_list in song_list_zz:
    print(song_from_list)

print("-" * 60)

for song_from_list in song_list_jim:
    print(song_from_list)

# for album_from_list in album_list:
#     print(album_from_list)
