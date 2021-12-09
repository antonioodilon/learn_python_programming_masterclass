# Searched about the replace() and translate() methods for this exercise, and
# found they are very useful:
# https://www.journaldev.com/23674/python-remove-character-from-string

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

new_text_2 = set(text.replace("\n", " ").split(" "))
print(new_text_2)

# If you want to split a string X number of numbers, then write text.split(" ", x):
# print(text.split(" ", 2))

# My best solution, I believe:
preps_used = set(text.replace("\n", " ").split(" ")).intersection(prepositions)
print(preps_used)

# Another solution, but not as good:
new_text = set(text.replace("\n", " ").split(" "))
print(new_text)
preps_used_2 = new_text.intersection(prepositions)
print(preps_used_2)

# Another solution:
preps_used_3 = set(text.replace("\n", " ").split(" ")) & prepositions
print(preps_used_3)


# preps_used = set(text.split(" "))
# print(preps_used)