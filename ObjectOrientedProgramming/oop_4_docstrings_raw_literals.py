class Song:
    """
    Class to represent a song.

    Attributes:
        title (str): Title to represent a song. Type is string.
        artist (str): Represents the song's creator. Type is string.
        duration (int): Represents the duration of the song in seconds.
        Type is integer and may be zero.
    """
    def __init__(self, title, artist, duration=0):
        """
        Song init method.

        :param title: Type `str`. Initialises the `title` attribute
        :param artist: Type `str`. It's the `artist` object representing
        the song's creator.
        :param duration: Type `int`. Initial value for the `duration`
        attribute. It is optional and defaults to zero if no value is
        specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


# Getting help from Python:
help(Song)  # Getting help for the Song class and its methods.
print("-" * 80)
help(Song.__init__)
print("-" * 80)
print(Song.__doc__)  # Prints the documentation specific for the class Song
print("-" * 80)
print(Song.__init__.__doc__)  # Prints the documentation specific for the
# __init__ method