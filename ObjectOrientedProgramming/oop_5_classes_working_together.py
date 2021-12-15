# When watching this class I changed my mind and decided to create my own
# classes instead of using Tim Buchalka's idea involving songs and albums

# Class Film will work together with the class StreamingService. One will
# be able to add films to a streaming service, in other words.
class Film:
    """
    Class to represent a film.

    Attributes:
        title(str): Title represents the film's name.
        director(str): Represents the film's director.
        duration(int): Represents the film's duration in minutes. Defaults
        to zero if no duration is specified.
    """

    def __init__(self, title: str, director: str, duration: int = 0):
        self.title = title
        self.director = director
        self.duration = duration


class StreamingService:
    """
    Class to represent a streaming service of films, using a list of
    available film titles.

    Attributes:
        streaming_name(str): The name of the streaming service.
        year(int): The year the streaming service was released.
        creator(str): Defaults to None. The name of the creator of the
        streaming service. If the creator wasn't one person, but a group
        of people, then creator is set to "Various".
        films(list[Film]): A list of films available in the application.
    """

    def __init__(self, streaming_name: str, year: int, creator: str = None):
        self.streaming_name = streaming_name
        self.year = year
        if creator is None:
            self.creator = "Various"
        else:
            self.creator = creator
        self.films = []

    def add_film(self, film: str, position=None):
        """
        Adds film titles to a list of films defined in the __init__ method.

        :param film: `str`. The film to be added to the films list.
        :param position: The position that the film will be added in the
        list's index. It is optional, and if not specified, will be added
        to the end of the list
        :return:
        """
        if position is None:
            self.films.append(film)
        else:
            self.films.insert(position, film)


if __name__ == "__main__":
    lynch_streaming_serv = StreamingService("AwesomeFlix", 2015, "Jonathan "
                                                                 "Grape")
    print(lynch_streaming_serv.streaming_name)
    print(lynch_streaming_serv.year)
    print(lynch_streaming_serv.creator)








