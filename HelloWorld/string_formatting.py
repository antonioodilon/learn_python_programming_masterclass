for i in range(1, 13): #Number 12 is not included!
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

print()

#Now let's establish some width of 2, 3 and 4 in the spaces so that the formatting looks better
for i in range(1, 13): #Number 12 is not included!
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))

print()

#Left-aligning the values using < and center-aligning using ^
for i in range(1, 13): #Number 12 is not included!
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

print()

print("Pi is approximately {0}".format(22 / 7))
print()
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7)) #f = with a standard precision of 6 decimals
print("Pi is approximately {0:52.50f}".format(22 / 7)) #52 = A width of 52; 50f = with a precision of 50 decimals'
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7)) #Python doesn't work with more than 51 decimals

print()
for i in range(1, 13): #Number 12 is not included!
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
    #If you don't specify a field number, Python will work with things in order.