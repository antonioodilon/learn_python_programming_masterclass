class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.initial_hit_points = self.hit_points  # Tim said that in the next video
        # (overriding methods), we would fix a bug that wouldn't reset the
        # self.hit_points to its original value whenever self.lives was greater
        # than zero. So I came up with my own solution. See line 23 as well
        self.lives = lives
        self.alive = True

    def take_damage(self, damage_taken):
        remaining_points = self.hit_points - damage_taken
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("{0} has taken {1} points of damage and has {2} points left"
                  .format(self.name, damage_taken, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = self.initial_hit_points
            if self.lives > 0:
                print("{0.name} has lost a life".format(self))
            else:
                print("You have killed {0.name}".format(self))
                self.alive = False

    def __str__(self):
        return "Name: {0.name} ; Hit points: {0.hit_points} ; Lives: {0.lives}," \
               " Alive: {0.alive}".format(self)


class Drow(Enemy):
    def __init__(self, name, house_name):
        # Calling Drow's superclass, Enemy:
        super().__init__(name=name, hit_points=25, lives=2)
        # super(Drow, self).__init__(name=name, hit_points=25, lives=2)
        # Another way of writing a subclass. The one above is better, though
        self.house_name = house_name

    def battle_cry_lolth(self):
        print("I'm {0} {1}!\nIn the name of Lolth, we fight!"
              .format(self.name, self.house_name))


class Druchii(Enemy):  # As part of the challenge, creating a new enemy class
    def __init__(self, name, faction):
        super().__init__(name=name, hit_points=20, lives=3)
        self.faction = faction