fantasy_characters = []
# Appending a list with the contents from a text file

with open("fantasy characters.txt", "r") as f_characters:
    for char in f_characters:
        fantasy_characters.append(char.strip("\n"))
        # Now we've removed \n, and it causes the next char to appear in
        # the line right after the previous one

for char in fantasy_characters:
    print(char)

print(fantasy_characters)

# strip() removes characters from the beginning or end of a line, and only
# from the beginning or end.

print("Minsc".strip("M"))