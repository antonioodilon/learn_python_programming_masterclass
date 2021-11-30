#Question 2
meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1)
print()
print(meal2)
print()
print(meal3)
print()
print(meal4)

print()

#Question 3
print("Greg\tJohn\tJane")

print()

#Question 5

a = 45
b = 15
c = 3

print(a - b / c)
#The output is a float because a division operation results in a float

print()

#Question 6
quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)

print()

#Question 7
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

print()

#Question 8
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])

print()

#Question 9
flower = "blue violet"
print("blue" in flower)

print()

#Question 10
flower = "rose"
colour = "red"

print("The {0} is {1}".format(flower, colour))