day = "Saturday"
day_period = "Afternoon"
location = "Beach"
temperature = 32
sunny = True

#Situation 1
if (day == "Saturday" and day_period == "Afternoon" and location == "Beach" and temperature > 26) or sunny == True:
    print("Go to Pipa Boat Party!")
else:
    print("Go to a night party!")

print("-" * 80)

#Situation 2
if (day == "Friday" and day_period == "Morning" and location == "Beach" and temperature > 26) or not sunny:
    print("Go to a night party!")
else:
    print("Go to Pipa Boat Party!")

print("-" * 80)

#Situation 3
day_2 = "Saturday"
day_period_2 = "Morning"
location_2 = "Beach"
temperature_2 = 32
sunny_2 = False

if day_2 == "Friday" or (day_period_2 == "Morning" and location_2 == "Beach") or (temperature_2 > 30 and sunny_2 == True):
    print("Go to Pipa Boat Party!")
else:
    print("Go to a night party!")
#Always remember that and has a higher precedence than or