import pytz
import datetime

for country in pytz.country_names:
    print(country, ": ", pytz.country_names[country], end=": ")
    if country in pytz.country_timezones:
        for local_timezone in pytz.country_timezones[country]:
            tz_to_display = pytz.timezone(local_timezone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(local_timezone, local_time))
# Printing the exact hour and date for each timezone in each country
    else:
        print("\t\tNo timezone defined")

# end= :
# "Python’s print() function comes with a parameter called ‘end’. By default,
# the value of this parameter is ‘\n’, i.e. the new line character. You
# can end a print statement with any character/string using this parameter."
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/