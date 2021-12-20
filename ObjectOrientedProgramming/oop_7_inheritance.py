# Inheritance is a powerful, but sometimes overused, tool in OOP. There
# are advantages, such as being able to write code only once, as each
# subclass will inherit the characteristics of their superclasses.
# On the other hand, if used inappropriately, they can make our code
# confusing and/or unnecessarily complex.

# Now we are going to create a superclass called Enemy and subclasses so
# we can use with the class Player previously defined

class Enemy:  # Since everything in Python is an object, Enemy is also a subclass
    # of a built-in superclass in Python. You can also write it as: class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage_taken):
        remaining_points = self.hit_points - damage_taken
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("{0} has taken {1} points of damage and has {2} points left"
                  .format(self.name, damage_taken, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name} ; Hit points: {0.hit_points} ; Lives: {0.lives}"\
            .format(self)


class Drow(Enemy):  # Python recommends that we put 2 blank lines between classes
    pass