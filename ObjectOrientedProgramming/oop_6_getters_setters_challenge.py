# The player's score increases by 1000 everytime their level increases by 1
# If the player drops back a level, they lose 1000 score for each level
# The cannot go below level 1


class Player(object):
    def __init__(self, name, level, score):  # level=1
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

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
            self.score += change * 1000
            self._level = level
        else:
            print("Level cannot be less than 0")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name} ; Lives: {0.lives} ; Level: {0.level} ;" \
               " Score: {0.score}".format(self)
# Junk code:
    # def _get_score(self):
    #     return self.score
    #
    # def _set_score(self, level):
    #     self.level = level
    #     while self.level >= 1:
    #         self.score += 1000
    #     # if self.level > 1:
    #     #     self._score += 1000
    #     # elif self.level <= 1:
    #     #     self._score = 0
    #
    # score1 = property(_get_score, _set_score)