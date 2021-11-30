#Be careful! "range" is a reserved word in Python, so if you name the file "range", you may get problems!

for i in range(7,32,3):
    print("The number is now {}: ".format(i))

print("-" * 80)

#Using a negative step value:
for i in range(21,0,-3):
    print("The number is now {}: ".format(i))

#for i in range(0,10):
#    print("The number is now {}: ".format(i))

print("-" * 80)

for i in range(30, 0, -1):
    if i % 2 == 0:
        print("The number {0} is divisible by 2".format(i))
#Printing numbers that are divisible by 2

print("-" * 80)

for i in range(100, 0, -1):
    if i % 7 ==0:
        print("The number {0} is divisible by 7".format(i))
#Printing numbers that are divisible by