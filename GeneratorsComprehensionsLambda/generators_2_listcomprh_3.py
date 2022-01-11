text = "i shall be the high-handed slayer!"
# Since strings are iterable, we can iterate over a string

capitals = [character.upper() for character in text]
print(capitals)

words = [word.upper() for word in text.split(sep=" ")]
print(words)
print([word.upper() for word in text.split(sep=" ")])  # We can also put the
# list comprehension directly inside the print() statement

lowercase_words = text.split(sep=' ')
# .split returns a list, so there is no need to use a list comprehension
# if we just want the words in lowercase
print(lowercase_words)