with open("fictional musician.txt", "r") as fict_musician:
    contents = fict_musician.readline()

musician = eval(contents)

print(musician)

title, artist, year, song = musician
print(title)
print(artist)
print(year)
print(song)

# Careful when using eval() !!

"""
eval is a built-in- function used in python, eval function parses the expression
argument and evaluates it as a python expression. In simple words, the eval
function evaluates the “String” like a python expression and returns the result
as an integer.
"""