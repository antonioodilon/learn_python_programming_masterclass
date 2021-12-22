import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage_taken):
        remaining_points = self._hit_points - damage_taken
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{0} has taken {1} points of damage and has {2} points left"
                  .format(self._name, damage_taken, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} has lost a life".format(self))
            else:
                print("You have killed {0._name}".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name} ; Hit points: {0._hit_points} ; Lives: {0._lives}," \
               " Alive: {0._alive}".format(self)


class Drow(Enemy):

    def __init__(self, name, house_name):
        super().__init__(name=name, hit_points=25, lives=2)
        self.house_name = house_name

    def battle_cry_lolth(self):

        print("I'm {0} {1}!\nIn the name of Lolth, we fight!"
              .format(self._name, self.house_name))


class Druchii(Enemy):

    def __init__(self, name, faction):
        super().__init__(name=name, hit_points=20, lives=3)
        self.faction = faction

    def parry(self):
        parry_value = random.randint(1, 30)
        # damage_taken = damage_taken
        if parry_value % 2 == 0 or parry_value % 5 == 0:
            print("--- {0._name} has parried your attack ---".format(self))
            return True
        else:
            return False
            # damage_taken = damage_taken
            # self.take_damage(-int(damage_taken))

    def take_damage(self, damage_taken):  # Now we are going to modify this
        # method slightly, so that it behaves a little differently for Druchii.
        # First, call the method by its exact name.
        if not self.parry():
            super().take_damage(damage_taken=damage_taken)  # Calling the
            # superclass' method, but modifying it slightly


        # This is approximately the code Tim wrote. He just wrote the method
        # as "dodge" instead of "parry"
        # if random.randint(1, 3) == 3:
        #     print("--- {0.name} has parried your attack ---")
        #     return True
        # else:
        #     return False