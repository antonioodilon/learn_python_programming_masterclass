splitString = "This string \nhas been \nsplit \nseveral times \nall right?"
print(splitString)

print()

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print()

#Escaping the quotation marks:
print('The pet shop owner said "Yeah, \'e\'s uh... Oh, he\'s sleeping."')
#or
print("The pet shop owner said \"Yeah, 'e's uh... Oh, he's sleeping.\"")
#or
print("""The pet shop owner said "Yeah, 'e's uh... Oh, he's sleeping." """)

print()

print("""The pet shop owner said "Yeah, \
'e's uh... Oh, he's sleeping." """)

print()

anotherSplitString = """This string has been
split
in
several
lines"""

print(anotherSplitString)
print()
#Escaping the end of the line?
splitString3 = """This string has been \
split \
in \
several \
lines"""

print(splitString3)

print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")

print()

print("C:\tonhoscomputer\notes.txt")
print()
#Solving this problem:
print("C:\\tonhoscomputer\\notes.txt")
print()
#or with raw strings (r)
print(r"C:\tonhoscomputer\notes.txt")
#The first method is better