# In other languages, such as Java and C++, different classes need to be
# stored in different files. In Python, on the other hand, it is unnecessary
# to do that. The best thing to do is to put related classes in the same file.

# According to Tim, in Python getters and setters are usually not necessary,
# but they are there if you need them. A different thing happens in languages
# such as Java (according to him), for instance.

# A setter is a method used to set the value of the data class attribute

# Creating a videogame. The first class we need is the player

class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3  # Hiding the lives attribute with an underscore.
        # It gives the users of our class an indication that they shouldn't
        # be calling it.
        self.level = 1
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

    lives = property(_get_lives, _set_lives)
# Take a look at the source code for property()!

# Try renaming self._lives to self.lives and you'll get an error in oop_6_getters_setters_2
# RecursionError: maximum recursion depth exceeded
# That's because lives = property(etc) (line 33) shares the same name as
# the attribute.

# Interestingly, if you rename lives = property(etc) to lives1 = property(etc),
# the code in oop_6_getters_setters_2 will work, but the user is not able to
# change lives to a negative number. In other words, _set_lives doesn't
# work as it should

    def __str__(self):
        return "Name: {0.name} ; Lives: {0.lives} ; Level: {0.level} ;" \
               " Score: {0.score}".format(self)  # => This code is a lot more
        # readable than the one below. Because we are referring to a class,
        # we don't need to write self.name, self.lives etc
        # return "Name: {0} ; Lives: {1} ; Level: {2} ; Score: {3}"\
        #     .format(self.name, self.lives, self.level, self.score)