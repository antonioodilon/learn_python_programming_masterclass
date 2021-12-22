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

    def __init__(self, name, faction, hit_points=20):  # Had to change this line
        # and add hit_points = 20
        super().__init__(name=name, hit_points=hit_points, lives=3)  # Also
        # changed this line to hit_points=hit_points so that Druchii has
        # its own hit_points that can be modified in any of its subclasses
        self.faction = faction

    def parry(self):
        parry_value = random.randint(1, 30)
        if parry_value % 2 == 0 or parry_value % 5 == 0:
            print("--- {0._name} has parried your attack ---".format(self))
            return True
        else:
            return False

    def take_damage(self, damage_taken):
        if not self.parry():
            super().take_damage(damage_taken=damage_taken)


# Challenge: create a subclass of Vampyre called VampyreKing that has 140
# hit_points, and only takes 1/4 of the damage. In my case, Vampyre = Druchii,
# and VampyreKing = DruchiiMonarch
class DruchiiMonarch(Druchii):

    def __init__(self, name, faction):
        super().__init__(name=name, faction=faction, hit_points=140)
        self.faction = faction

    def take_damage(self, damage_taken):
        return super().take_damage(damage_taken / 4)


# Code that Tim wrote was similar to this:
class DruchiiMonarch2(Druchii):

    def __init__(self, name, faction):
        super().__init__(name, faction=faction)
        self._hit_points = 140

    def take_damage(self, damage_taken):
        return super().take_damage(damage_taken // 4)  # Integer division by 4