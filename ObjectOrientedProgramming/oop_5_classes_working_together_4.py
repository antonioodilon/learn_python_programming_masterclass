# Significant changes have been made in this code in comparison with the
# previous one. load_data(), for example, is now much smaller, and a new
# add_song() method has been created in the class Artist (before that there
# already was an add_song() method, but it belonged to the class Album.

class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title  # If we type self.name = title, the program will crash
        # Because find_object expects name, not title: if item.name == field
        self.artist = artist
        self.duration = duration

    # This is where getters, setters and property come into place.
    # Google: getters, setters, property Python
    # Very useful to take this approach if your code will be used by others.
    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist: (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]):  A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song_album(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): The title of the song to add
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        song_to_find = find_object(song, self.tracks)
        if song_to_find is None:
            song_to_find = Song(song, self.artist)
            if position is None:  # If the song doesn't have a specific position in the tracklist
                self.tracks.append(song_to_find)
            else:  # If the song does have a specific position
                self.tracks.insert(position, song_to_find)
        # Remember that Python lists have the insert() method.
        # The insert() method inserts an item in specified position inside
        # a list. Different from append()
        # https://www.w3schools.com/python/ref_list_insert.asp


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not added again
                (although this is yet to implemented).
        """
        self.albums.append(album)

    # Creating a new add_song method, but this time named as add_song_artist
    # to differentiate between this method in this class and the one created
    # in the Album class:
    def add_song_artist(self, name, year, title):
        """
        Adds a new song to the collection of albums. This method adds a
        new album to the collection; if the album doesn't already exist
        there, a new album will be created.

        :param name: `str`
        :param year: `int`
        :param title: `str`
        :return:
        """
        album_to_find = find_object(name, self.albums)
        # if album_to_find is None: # -> Code that Tim wrote
        if album_to_find not in self.albums:
            print("{} not found".format(name))
            album_to_find = Album(name, year, self)
            self.add_album(album_to_find)
        else:
            print("Found album {}".format(name))

        album_to_find.add_song_album(title)  # Remember that album_to_find
        # is an object with the Album class. Thus, it doesn't have an add_song_artist
        # method, but an add_song_album method.


def find_object(field, object_list):
    """Check object_list to see if there is a field there with the same
    name attribute as the item. If so, return the item"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    # We've removed the new_artist and new_album variables from the function

    artist_list = []

    with open("albums_original.txt", "r") as album_file:
        for line in album_file:
            # Unpacking the tuple below:
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            # We've also removed many of the conditions related to new_artist, new_album
            # and new_song:
            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            # A new add_song method, which was created inside the Artist class
            new_artist.add_song_artist(album_field, year_field, song_field)

    return artist_list


def create_check_file(artist_list):
    with open("check_file_3.txt", "w") as check_file_4:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}"  # Before it was {2.title}
                          .format(new_artist, new_album, new_song),
                          file=check_file_4)


if __name__ == "__main__":
    artists_processed = load_data()
    print(type(artists_processed))
    print("There are {} artists".format(len(artists_processed)))
    create_check_file(artists_processed)
