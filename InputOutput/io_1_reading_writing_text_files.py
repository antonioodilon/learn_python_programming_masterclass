jabber = open("R:\\Antonio\\1_Coding\\sample.txt", "r")
# Put two slashes \\ so that Python can understand that characters like
# \n and \t should be ignored, and that this is really a path in the computer.

# You can also put the file in your projects folder

for line in jabber:
    if "beware" in line.lower():  # lower() to consider the text as if it were
        # lowercase
        print(line, end="")

jabber.close()

print("-" * 80)

# with allows us to write less and it's cleaner. Also, no need to call the
# .close() method in the end
with open("R:\\Antonio\\1_Coding\\sample.txt", "r") as jabber2:
    for line in jabber2:
        if "VORP" in line.upper():
            print(line, end="")

print("-" * 80)

# Printing the entire poem this time:
with open("R:\\Antonio\\1_Coding\\sample.txt", "r") as jabber3:
    line = jabber3.readline()
    while line:
        print(line, end="")
        line = jabber3.readline()  # Reading from the first to the last line

print("-" * 80)

with open("R:\\Antonio\\1_Coding\\sample.txt", "r") as jabber4:
    lines = jabber4.readlines()
print(lines)  # Notice that the output has \n to indicate a new line. This
# is very useful for debugging purposes, so it may be very useful to print
# it like this.
print(type(lines))  # The lines of the poem are in a list called lines

for line in lines:
    print(line, end="")

print("-" * 80)

with open("R:\\Antonio\\1_Coding\\sample.txt", "r") as jabber4:
    lines = jabber4.readlines()
print(lines)

for line in lines[5:0:-1]:  # Printing backwards, starting on line at index
    # position 5 and up to, but not including, line at index position 0
    print(line, end="")

print("-" * 80)

with open("R:\\Antonio\\1_Coding\\sample.txt", "r") as jabber4:
    lines = jabber4.read()  # Now the words are being read backwards. That's
    # the difference between readlines() and read()

for line in lines[::-1]:
    print(line, end="")