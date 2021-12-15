import datetime
import pytz


class FactionArmy:
    """A simple army for a faction in a fictional strategy videogame"""

    # Implementing a static method. It is not supposed to be used outside
    # of the class, so whoever decides to do so will do it at their own
    # risk
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, number_warriors, culture):
        self._name = name
        self._number_warriors = number_warriors
        self._culture = culture
        self.recruitment_list = [(FactionArmy._current_time(), number_warriors)]
        # By using a tuple we guarantee that the values inside won't be changed,
        # so the initial number of warriors will always be there.
        print("Your faction's name is {} and your culture is {}."
              .format(self._name, self._culture))
        self.show_number_warriors()

    def replenishment(self, reinforcements):
        if reinforcements > 0:
            print("You have been reinforced by {} warriors".format(reinforcements))
            self._number_warriors += reinforcements
            print("You now have {} soldiers after reinforcements"
                  .format(self._number_warriors))
            self.recruitment_list.append \
                ((FactionArmy._current_time(), reinforcements))
            # We are displaying when, in UTC time, the reinforcements have
            # been added to the faction's army. It is a list with a series
            # of tuples
            self.show_number_warriors()
            print("-" * 80)

    def losses(self, lost_warriors):
        if 0 < lost_warriors <= self._number_warriors:
            print("You have lost {} warriors in battle".format(lost_warriors))
            self._number_warriors -= lost_warriors
            print("After the last battle you now have {} soldiers"
                  .format(self._number_warriors))
            self.recruitment_list.append \
                ((FactionArmy._current_time(), -lost_warriors))
            self.show_number_warriors()
            print("-" * 80)
        else:
            print("You can't lose more warriors than the ones you currently "
                  "have!".format(self._name))
            self.show_number_warriors()
            print("-" * 80)

    def show_number_warriors(self):
        print("Your army has {} warriors".format(self._number_warriors))
        print("-" * 80)

    def show_number_changes(self):
        for date, number_change in self.recruitment_list:
            if number_change > 0:
                change_type = "recruited"
            elif number_change == 0:
                change_type = ""
            else:
                change_type = "lost"
                number_change *= -1  # If you don't write this line of code,
                # the output will show "-200 lost on" instead of "200 lost on"
            print("{:6} {} on {} (local time was {})"
                  .format(number_change, change_type, date, date.astimezone()))
            print("-" * 80)

    def change_culture(self, culture):
        self._culture = culture
        print("Your faction's culture is now {}".format(self._culture))
        print("-" * 80)


if __name__ == "__main__":
    chaos_dwarves = FactionArmy("Chaos Dwarves", 200, "Chaosw")
    chaos_dwarves.show_number_warriors()
    chaos_dwarves.replenishment(500)
    chaos_dwarves.losses(150)
    chaos_dwarves.replenishment(60)
    # chaos_dwarves.number_warriors = 500  # Instead of 610, it is showing 500
    # # warriors. Nothing stops the user from changing this number, so we have
    # # to deal with that. So in the __init__ method we changed self.name to
    # # self._name (putting an underscore before name). Now if we try to run
    # # chaos_dwarves.number_warriors = 500, the output will correctly show
    # # 610 warriors instead of 500
    chaos_dwarves._number_warriors = 500  # But if we run this, it will show
    # 500 instead of 610. The rule is: one underscore is for internal usage
    # only. Python doesn't stop you from doing it if you decide to change it,
    # but things will probably break if you leave it as it is and not change
    # it to chaos_dwarves.number_warriors = 500 (without the initial underscore)
    chaos_dwarves.show_number_changes()
    chaos_dwarves.show_number_warriors()