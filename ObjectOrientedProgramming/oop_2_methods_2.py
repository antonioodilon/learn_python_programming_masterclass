# Now we are going to show when the warriors have been added to the faction's
# army

import datetime
import pytz


class FactionArmy:
    """A simple army for a faction in a fictional strategy videogame"""

    def __init__(self, name, number_warriors, culture):
        self.name = name
        self.number_warriors = number_warriors
        self.culture = culture
        print("Your faction's name is {}, and your culture is {}"
              .format(self.name, self.culture))
        self.recruitment_list = []

    def replenishment(self, reinforcements):
        if reinforcements > 0:
            print("You have been reinforced by {} warriors".format(reinforcements))
            self.number_warriors += reinforcements
            print("You now have {} soldiers after reinforcements"
                  .format(self.number_warriors))
            self.recruitment_list.append\
                ((pytz.utc.localize(datetime.datetime.utcnow()), reinforcements))
            # We are displaying when, in UTC time, the reinforcements have
            # been added to the faction's army. It is a list with a series
            # of tuples
            self.show_number_warriors()
            print("-" * 80)

    def losses(self, lost_warriors):
        if 0 < lost_warriors <= self.number_warriors:
            print("You have lost {} warriors in battle".format(lost_warriors))
            self.number_warriors -= lost_warriors
            print("After the last battle you now have {} soldiers"
                  .format(self.number_warriors))
            self.show_number_warriors()
            print("-" * 80)
        else:
            print("You can't lose more warriors than the ones you currently "
                  "have!".format(self.name))
            self.show_number_warriors()
            print("-" * 80)

    def show_number_warriors(self):
        print("Your army has {} warriors".format(self.number_warriors))
        print("-" * 80)

    def show_number_changes(self):
        for date, number_change in self.recruitment_list:
            if number_change > 0:
                change_type = "recruited"
            else:
                change_type = "lost"
                number_change *= -1
            print("{:6} {} on {} (local time was {})"
                  .format(number_change, change_type, date, date.astimezone()))
            print("-" * 80)

    def change_culture(self, culture):
        self.culture = culture
        print("Your faction's culture is now {}".format(self.culture))
        print("-" * 80)


if __name__ == "__main__":
    warriors_chaos = FactionArmy("Warriors of Chaos", 0, "Chaos")
    # warriors_chaos.change_culture() -> Missing one positional argument
    warriors_chaos.show_number_warriors()  # Checking how many warriors we have
    # at the moment
    warriors_chaos.replenishment(1000)
    warriors_chaos.losses(200)
    # warriors_chaos.show_number_warriors() -> Now we don't need this anymore
    # because the self.show_number_warriors() has been added to the self.losses()
    # and self.replenishment() methods.
    warriors_chaos.losses(900)
    warriors_chaos.show_number_changes()
    warriors_chaos.change_culture("Warriors of Khorne")
    print(warriors_chaos.recruitment_list)