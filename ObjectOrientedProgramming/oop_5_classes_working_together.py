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
    Class to represent a streaming service of films dedicated to a director,
     using a list of available film titles.

    Attributes:
        streaming_name(str): The name of the streaming service.
        year(int): The year the streaming service was released.
        director(str): Defaults to None. The name of the director to which
        the streaming service is dedicated to. If the director wasn't one
         person, but a group of people, then it is set to "Various".
        films(list[Film]): A list of films available in the application.

    Methods:
        add_film: Used to add a new film to the film list.
    """

    def __init__(self, streaming_name: str, year: int, director: str = None):
        self.streaming_name = streaming_name
        self.year = year
        if director is None:
            self.director = Director("Various")
        else:
            self.director = director
        self.films = []

    def add_film(self, film: str, position=None):
        """
        Adds film titles to a list of films defined in the __init__ method.

        :param film (Film): `str`. The film to be added to the films list.
        :param position: The position that the film will be added in the
        list's index. It is optional, and if not specified, will be added
        to the end of the list
        :return:
        """
        if position is None:
            self.films.append(film)
        else:
            self.films.insert(position, film)


class Director:
    """
    Class that stores the director's details.

    Attributes:
        name(str): The director's name.
        films: A list that stores the films this person directed or took
        part in.

    Methods:
        add_film: Adds a new film that this director participated in to the
         list films.
    """

    def __init__(self, name:str):
        self.name = name
        self.films = []

    def add_films(self, film):
        """
        Adds a new film to the list films defined in the __init__ method.
        TODO: If the film is already present in the list, it will not be added
        again (this is yet to be implemented)

        :param film:
        :return:
        """
        self.films.append(film)


if __name__ == "__main__":
    awesome_flix = StreamingService("AwesomeFlix", 2015, "David Lynch")
    print(awesome_flix.streaming_name)
    print(awesome_flix.year)
    print(awesome_flix.director)








