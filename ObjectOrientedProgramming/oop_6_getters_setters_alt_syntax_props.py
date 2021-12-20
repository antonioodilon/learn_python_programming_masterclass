class Player(object):
    def __init__(self, name):  # level=1
        self.name = name
        self._lives = 3
        self._xp = 0
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        self._lives = lives
        if self._lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be less than zero.")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        change = level - self._level
        if level > 0:
            self._score += change * 1000
            self._level = level
        else:
            print("Level cannot be less than 0")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # Below we have alternate syntax for properties:
    @property  # Notice that we've refactored self.score to self._score
    def alt_score(self):
        return self._score

    @alt_score.setter
    def alt_score(self, new_score):
        self._score = new_score
    # This method and the one above both need to have the same name

    @property
    def alt_xp(self):
        return self._xp

    @alt_xp.setter
    def alt_xp(self, new_xp):
        self._xp = new_xp

    def __str__(self):
        return "Name: {0.name} ; Lives: {0._lives} ; Level: {0._level} ;" \
               " Score: {0._score}; XP: {0._xp}".format(self)