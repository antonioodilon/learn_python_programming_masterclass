# Unlike statically typed languages, like Java, Python isn't really that interested
# in the specific types of the objects. It is more interested in how the
# objects behave. So if two different objects behave in the same way in a
# particular situation, as far as Python is concerned, both objects are the
# same in that situation.

# In our example below, we've created two different classes, each one being
# a different object. However, because both classes have the same methods,
# as far as Python is concerned, both are the same, as both behave the same.

# Again a reference to the Warhammer fantasy universe:
class WarriorOfKhorne(object):

    def swing_axe(self):
        print("I will claim your skull for the Blood God!")

    def swing_mace(self):
        print("Smash this weakling, so that Khorne may favour me!")

    def swing_sword(self):
        print("I will sharpen my sword with your skull!")


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
    test_warrior_of_khorne(WarriorOfKhorne)

    print("-" * 60)

    dinin_dourden = DrowWarrior()
    test_warrior_of_khorne(DrowWarrior)
    # So even though Dinin Do'Urden is not a Warrior of Khorne (in fact,
    # warriors of Khorne and drow warriors belong to different universes
    # entirely), as far as Python is concerned it is a warrior of Khorne
    # because it has the same methods that test_warrior_of_khorne() has.