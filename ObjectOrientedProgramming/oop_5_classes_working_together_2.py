class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


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

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as album_file:
        for line in album_file:
            # Unpacking the tuple below:
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip("\n").split("\t"))
            # Applying the strip() and split() methods to each string and unpacking
            # as a tuple
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)
            # print(type(line))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:  # If we want to add a new artist and this
                # artist is not in the file albums.txt
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                # Creating an object using the class Artist and its attributes
                new_album = None
# If you have any doubts about the codes above and below, take a look at the
# code oop_2_methods_3, on line 85 where it says warriors_chaos.show_number_warriors().
# Basically:
# FactionArmy = Artist -> The class name
# "Warriors of Chaos", 0, "Chaos" = artist_field -> The parameters related to the
    # attributes. FactionArmy, in its __init__ (constructor) method has 3
    # attributes, and thus must receive 3 parameters. Artist, on the other hand,
    # has 1 attribute (name), and thus receives only one parameter.
# warriors_chaos = new_artist , and
# show_number_warriors() = add_album

            # If we want to add a new album and this album is not present:
            if new_album is None:
                new_album = Album(album_field, year_field, song_field)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, song_field)
                # Creating an object using the class Album and its attributes

            # Now adding the songs:
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # Finally, we will store the last bit of data that wasn't processed
        # in our list
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_check_file(artist_list):
    with open("check_file.txt", "w") as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}"
                          .format(new_artist, new_album, new_song),
                          file=check_file)


if __name__ == "__main__":
    artists_processed = load_data()
    print(type(artists_processed))
    print("There are {} artists".format(len(artists_processed)))
    # for artist_name in artists_processed:
    #     print(artist_name)
    create_check_file(artists_processed)  # Up there we equalled the list
    # or artists in albums.txt to the load_data() function, and called it
    # artists_processed. So the parameter for the function create_check_file,
    # which will print all that information on the check_file.txt file, is
    # artists_processed

# Reviewing the strip() and split() methods:
# string1 = "This is a string, here"
# stringstrip = tuple(string1.strip().split())
# print(stringstrip)