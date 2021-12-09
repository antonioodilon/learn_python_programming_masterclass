import pytz
import datetime

print("Please choose a timezone of your preference (pressing 0 will quit the "
      "program):")
for country in pytz.all_timezones[0:10]:
    print("\t", country)

# user_choice = int(input("> "))
options = list(range(0, 11))
# Correct the small bug. Pressing 0 will display "Zulu", and then quit the
# program if 0 is pressed again

while True:
    user_choice = int(input("> "))
    if user_choice in options:
        options[user_choice] = pytz.all_timezones[0:10]
        # print(pytz.all_timezones[user_choice - 1])
        country = pytz.all_timezones[user_choice - 1]
        target_timezone = datetime.datetime.now(pytz.timezone(country))
        local_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
        # local_timezone = datetime.datetime.now()
        aware_utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        print("You have chosen", country)
        print("\tThe time and date in {}'s timezone is {}. Its timezone's name is {}"
              .format(country, target_timezone.strftime("%A %x %X %z"), target_timezone.tzinfo))
        print("\tThe time and date in your location is {}, and your timezone's name"
              " is {}".format(local_time.strftime("%A %x %X %z"), local_time.tzinfo))
        print("\tThe UTC time and date is {}, and its timezone name is {}"
              .format(aware_utc_time.strftime("%A %x %X %z"), aware_utc_time.tzinfo))
        # print("The time in {}'s timezone is {}".format(country, ))
        # print(pytz.all_timezones[user_choice - 1].datetime.datetime.now())
    # elif user_choice not in options:
    #     print("Please choose a valid option")
    #     pass
    elif user_choice == 0:
        # if country == "Zulu":
        #     pass
        print("The program will now quit")
        break
    else:
        print("Please choose a valid option: ")
        for country in pytz.all_timezones[0:10]:
            print("\t", country)

# if user_choice in pytz.all_timezones[0:10]:
#     print("well done")
# else:
#     print("fail")