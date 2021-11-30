#Revisiting the code in tuples_intro2
british = "Dead Sun", "British Murder Boys", 2011
schwefelgelb = "Bis Zum Nachsten Tag", "Schwefelgelb", 2016
liebing = "Tunox", "Chris Liebing", 1992
kruse = "Latin Lovers", "Monika Kruse", 2008
porto = "Sambassim", "Fernanda Porto", 2010

print(liebing)
print(liebing[0])
print(liebing[1])
print(liebing[2])

print("-"*80)

song, artist, year = liebing  # This makes the code much more readable,
# because now we know what each variable that we are using to unpack the
# tuple represents, instead of always memorizing what each index position
# actually represents
print(song)
print(artist)
print(year)

print("-"*80)

laptop = ("Acer", 20, 16, 3, 2450.87)
print(laptop[1]*laptop[2])

print("-"*80)

brand, width, length, height, price = laptop
print(width * length)  # Calculating the area of the surface in a much more
# readable way