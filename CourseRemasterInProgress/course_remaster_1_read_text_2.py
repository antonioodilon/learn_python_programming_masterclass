filename = 'Jabberwocky.txt'
with open(filename) as jabber:
    line_1 = jabber.readline().rstrip()  # readline() reads one line at a time,
    # and using the rstrip() method we strip everything to the right of the
    # first line
print(line_1)

print('=' * 80)

chars = "'"
no_apostrophe = line_1.strip(chars)
print(no_apostrophe)  # Now the line doesn't start with apostrophe

chars_2 = "'Twasebv"
no_chars_2 = line_1.strip(chars_2)  # strip() first processes the left-hand
# side of the string, and then the right-hand side. It understood that the
# characters ' , T, w, a, and s were in the far-left of the string and stopped
# processing when it saw that the whitespace before 'brillig' was not included
# in chars_2. Having evaluated the condition to false, it then moved to the
# right hand side of the string and evaluated that the characters v, e and s
# in 'toves' were inside chars_2. Since 'o' wasn't, the condition it wasn't stripped
# evaluated to false, and strip() didn't continue processing.
print(no_chars_2)

print('=' * 80)

chars_3 = "'Twasebvo"
no_chars_3 = line_1.strip(chars_3)
print(no_chars_3)

# This is what strip is doing on the left-hand side:
for character in line_1:
    if character in chars_2:
        print(f"Removing '{character}'")
    else:
        break

print('=' * 80)

# This is what strip is doing on the right-hand side:
for character in line_1[::-1]:
    if character in chars_2:
        print(f"Removing '{character}'")
    else:
        break

print('=' * 80)

twas_removed = line_1.removeprefix("'Twas")
print(twas_removed)
toves_removed = line_1.removesuffix("toves")
print(toves_removed)