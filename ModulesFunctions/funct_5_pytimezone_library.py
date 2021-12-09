import pytz
import datetime

print(pytz.all_timezones)  # To get the list of timezones in the pytz modules

print("-" * 80)

country1 = "Europe/Moscow"
country2 = "America/Maceio"
tz_to_display1 = pytz.timezone(country1)
local_time1 = datetime.datetime.now(tz_to_display1)
tz_to_display2 = pytz.timezone(country2)
local_time2 = datetime.datetime.now(tz_to_display2)

print("The local time and date in {0} is {1}".format(country1, local_time1))
print("The local time and date in {0} is {1}".format(country2, local_time2))
print("UTC now is {}".format(datetime.datetime.utcnow()))

print("-" * 80)

for country in pytz.all_timezones:
    print("The local time and date in {0} is {1}"
          .format(country, datetime.datetime.now(pytz.timezone(country))))
# To get the list of timezones in the pytz modules and their respective
# times and dates

print("-" * 80)

# print(type(pytz.country_names))
for country_code, country_name in sorted(pytz.country_names.items()):
    print(country_code, ": ", country_name)

for country in sorted(pytz.country_names):
    print(country, ": ", pytz.country_names[country], pytz.country_timezones
          .get(country))
    # Using the .get() method to get the different timezones of different
    # countries. Returns None if there isn't a value to get

# The code below didn't work as expected:
# for country_code1, country_name2 in sorted(pytz.country_names):
#     print(country_code1, ": ", country_name2, pytz.country_timezones.get(country_name2))