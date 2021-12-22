# Challenge: remove circular references. The Artist class can reference
# the Album class and the Album class can reference the Song class, but
# there must be no circular references. So, as far as I understand, the
# Song class can't reference the Artist class

# As it turns out, my initial assumption was wrong. By circular references,
# Tim meant that neither the Song class nor the Album class stored Artist
# objects.
# So for example, in the Album class, instead of self.artist = Artist("Various Artists"),
# we now have self.artist = "Various Artists"

# Notice, though, that Artist still references objects in Album (line 121), and Album
# still references objects in Song (line 72).

class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (str): The name of the song's creator
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist (str): The name of the artist. If not specified,the artist will
        default to an artist with the name "Various Artists".
        tracks (List[Song]):  A list of the songs on the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
            # self.artist = Artist("Various Artists") was unnecessary.
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
            if position is None:
                self.tracks.append(song_to_find)
            else:
                self.tracks.insert(position, song_to_find)


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
            album_to_find = Album(name, year, self.name)
            # The name of the album, the year, and the artist's name
            self.add_album(album_to_find)
        else:
            print("Found album {}".format(name))

        album_to_find.add_song_album(title)


def find_object(field, object_list):
    """Check object_list to see if there is a field there with the same
    name attribute as the item. If so, return the item"""
    for item in object_list:
        if item._name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums_original.txt", "r") as album_file:
        for line in album_file:
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song_artist(album_field, year_field, song_field)

    return artist_list


def create_check_file(artist_list):
    with open("check_file_4.txt", "w") as check_file_5:  # Creating a new
        # check_file because check_file_3 was being used by the previous code
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}"
                          .format(new_artist, new_album, new_song),
                          file=check_file_5)


if __name__ == "__main__":
    artists_processed = load_data()
    print(type(artists_processed))
    print("There are {} artists".format(len(artists_processed)))
    create_check_file(artists_processed)
