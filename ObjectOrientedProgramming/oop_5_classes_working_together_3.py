# Now we are going to make some changes to the code to make sure that Python
# understands which lines of code in check_file.txt are equal to albums.txt,
# despite them being in different lines.

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


def find_object(field, object_list):
    """Check object_list to see if there is a field there with the same
    name attribute as the item. If so, return the item"""
    for item in object_list:
        if item._name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
# Remember to compare albums_original.txt with check_file_2.txt to see the differences
    with open("albums_original.txt", "r") as album_file:
        for line in album_file:
            # Unpacking the tuple below:
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

        # The lines below are different from the corresponding ones in
        # oop_5_classes_working_togeter_2.py
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
        # Retrieve the artist object if there is one. Otherwise, create a
        # new artist object and add it to the artist list
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, song_field)
                new_artist.add_album(new_album)
        # Below we retrieve the album object if there is one. Otherwise,
        # create a new album object and add it to the artist list
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # We don't need the code below anymore:
        # if new_artist is not None:
        #     if new_album is not None:
        #         new_artist.add_album(new_album)
        #     artist_list.append(new_artist)

    return artist_list


# Remember to compare albums_original.txt with check_file_2.txt to see the differences
def create_check_file(artist_list):
    with open("check_file_2.txt", "w") as check_file_3:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}"
                          .format(new_artist, new_album, new_song),
                          file=check_file_3)


if __name__ == "__main__":
    artists_processed = load_data()
    print(type(artists_processed))
    print("There are {} artists".format(len(artists_processed)))
    create_check_file(artists_processed)