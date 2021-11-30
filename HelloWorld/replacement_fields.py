age = 30
print("My age is " + str(age) + " years old.")

#{} represents a replacement field
age2 = 30
print("My age is {0} years old.".format(age2))

#The usefulness of replacement fields:
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}."
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec.".format(31))

print()

# Keldorn is good, Jaheira is neutral, Xvar is evil, Neera is neutral, Yoshimo is neutral, Baelor is evil, Khalid is good
print("Keldorn is {0}, Jaheira is {1}, Xvar is {2}, Neera is {1}, Yoshimo is {1}, Baelor is {2}, Khalid is {0}"
      .format("Good", "Neutral", "Evil"))

print()

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, "
      "Dec: {2}".format(28, 30, 31))
# The position in the index determines which values go in which place

print()

print("""Keldorn: {0}
Jaheira: {1}
Xvar: {2}
Neera: {1}
Yoshimo: {1}
Baelor: {2}
Khalid: {0}""".format("Good", "Neutral", "Evil"))