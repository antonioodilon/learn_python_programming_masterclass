# Creating a class for the weapon halberd
class Halberd(object):

    def __init__(self, size):
        self.size = size

    def pierce_halberd(self):
        if self.size > 3:
            print("I have no problem fighting cavalry")
        elif 2 < self.size < 3:
            print("It's gonna be hard to fight horsemen")
        else:
            print("I can only fight infantry with this halberd")


class WarriorOfKhorne(object):

    def __init__(self):  # Creating a _weapon_halberd object and assigning
        # it to the Halberd class.
        self._weapon_halberd = Halberd(3.5)

    def swing_axe(self):
        print("I will claim your skull for the Blood God!")

    def swing_mace(self):
        print("Smash this weakling, so that Khorne may favour me!")

    def swing_sword(self):
        print("I will sharpen my sword with your skull!")

    def pierce_halberd(self):
        self._weapon_halberd.pierce_halberd()  # Any _weapon_halberd objects
        # we create will have the Halberd class and any methods this class
        # has, including pierce_halberd.


# Again a reference to the Dungeons and Dragons universe:
class DrowWarrior(object):

    def swing_axe(self):
        print("I will claim your skull for Lolth!")

    def swing_mace(self):
        print("Smash this weakling, so that The Spider Queen may favour me!")

    def swing_sword(self):
        print("I will sharpen my scimitar with your skull!")


def test_warrior_of_khorne(warrior_of_khorne):
    warrior_of_khorne.swing_axe(self=True)
    warrior_of_khorne.swing_mace(self=True)
    warrior_of_khorne.swing_sword(self=True)


if __name__ == "__main__":
    arbaal_the_undefeated = WarriorOfKhorne()
    arbaal_the_undefeated.pierce_halberd()
    print("-" * 80)
    test_warrior_of_khorne(WarriorOfKhorne)