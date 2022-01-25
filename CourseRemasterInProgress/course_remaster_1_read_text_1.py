with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())

print('=' * 80)

with open('Jabberwocky.txt', 'r') as jabber_2:
    lines_2 = jabber_2.readlines()  # .readlines() returns a list containing the
    # strings of our poem

print(lines_2)  # Notice that the whitespace is present in each element of the
# list as \n

print(lines_2[::-1])  # Printing in reverse order

for line_2 in reversed(lines_2):  # reversed() returns a reverse iterator
    print(line_2, end='')
# Be aware that using these techniques we are printing an entire text file.
# If it is too big, your computer's memory might not be able to handle it,
# but in this case it is your problem. Make sure you understand what the
# limitations of your computer are.

print('=' * 80)

# The default mode for with open() is to open a file for reading, if you don't
# specify one. So the code below this line will not be with open('Jabberwocky.txt', 'r'),
# with 'r' in the end
with open('Jabberwocky.txt') as jabber_3:
    text = jabber_3.read() # Now we have ONE string instead of a list
print(text)

print('=' * 80)

print(text[::-1])  # Printing all characters inside each line of the string
# in reverse order

print('=' * 80)

for character in reversed(text):
    print(character, end='')

print('=' * 80)

with open('Jabberwocky.txt') as jabber_4:
    while True:
        line = jabber_4.readline().rstrip()  # readline() is used for reading
        # each line
        print(line)
        if "callooh" in line.casefold():
            break  # Break out of the loop if we find a line with "callooh",
            # while also ignoring case

print('=' * 80)

with open('Jabberwocky.txt') as jabber_5:
    for line in jabber_5:
        print(line.rstrip())  # Different from line 43 (line = jabber_4.readline().rstrip()),
        # this doesn't mutate the string. It only prints out a copy that doesn't
        # end with a newline
        if "callooh" in line.casefold():
            break
