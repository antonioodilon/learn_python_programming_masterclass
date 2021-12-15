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
        self.__name = name
        self.__number_warriors = number_warriors
        self.__culture = culture
        self.recruitment_list = [(FactionArmy._current_time(), number_warriors)]
        # By using a tuple we guarantee that the values inside won't be changed,
        # so the initial number of warriors will always be there.
        print("Your faction's name is {} and your culture is {}."
              .format(self.__name, self.__culture))
        self.show_number_warriors()

    def replenishment(self, reinforcements):
        if reinforcements > 0:
            print("You have been reinforced by {} warriors".format(reinforcements))
            self.__number_warriors += reinforcements
            print("You now have {} soldiers after reinforcements"
                  .format(self.__number_warriors))
            self.recruitment_list.append \
                ((FactionArmy._current_time(), reinforcements))
            # We are displaying when, in UTC time, the reinforcements have
            # been added to the faction's army. It is a list with a series
            # of tuples
            self.show_number_warriors()
            print("-" * 80)

    def losses(self, lost_warriors):
        if 0 < lost_warriors <= self.__number_warriors:
            print("You have lost {} warriors in battle".format(lost_warriors))
            self.__number_warriors -= lost_warriors
            print("After the last battle you now have {} soldiers"
                  .format(self.__number_warriors))
            self.recruitment_list.append \
                ((FactionArmy._current_time(), -lost_warriors))
            self.show_number_warriors()
            print("-" * 80)
        else:
            print("You can't lose more warriors than the ones you currently "
                  "have!".format(self.__name))
            self.show_number_warriors()
            print("-" * 80)

    def show_number_warriors(self):
        print("Your army has {} warriors".format(self.__number_warriors))
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
        self.__culture = culture
        print("Your faction's culture is now {}".format(self.__culture))
        print("-" * 80)


if __name__ == "__main__":
    chaos_dwarves = FactionArmy("Chaos Dwarves", 200, "Chaos")
    chaos_dwarves.show_number_warriors()
    chaos_dwarves.replenishment(500)
    chaos_dwarves.losses(150)
    chaos_dwarves.replenishment(60)
    chaos_dwarves.__number_warriors = 500  # Now this value won't be accidentally
    # changed by the user, even though this line of code as two underscores
    chaos_dwarves.show_number_changes()
    chaos_dwarves.show_number_warriors()
    print(chaos_dwarves.__dict__)
    # chaos_dwarves._FactionArmy__number_warriors = 500  # If you REALLY want
    # to change it, though, this is how you go about it. There's no point
    # in doing it, though, as Tim explained.
    chaos_dwarves.show_number_warriors()