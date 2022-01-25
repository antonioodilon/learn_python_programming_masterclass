jabber = open('Jabberwocky.txt', 'r')  # Jabberwocky.txt: the name of the file
# we want to open

for line in jabber:
    # print(line, end='')  # With end='' we no longer get the extra line for each
    # line in the text
    # print(len(line))
    # print(line.strip())  # Stripping the newline character from each string
    # print(line.rstrip())  # Removing whitespace from the right
    print(line.lstrip())  # Removing whitespace from the left

jabber.close()
