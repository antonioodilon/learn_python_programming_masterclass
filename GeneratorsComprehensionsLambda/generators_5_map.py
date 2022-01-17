import re

# When passing a function as an argument to another function, you don't put
# the parentheses. You put the parentheses when you want the result of calling
# the function

text = "I shall be the high-handed slayer!"

chars = [char.upper() for char in text]
print(chars)

# map() takes two arguments:
# 1) First argument is a function
# 2) Second argument is any iterable

# map() calls the function for an item in the iterable and stores the result
# in a new iterable

# Using map to do the same thing
chars_map = list(map(str.upper, text))  # str.upper -> We are passing this
# function as an argument, so we don't put parentheses () !
print(chars_map)

# According to Tim, it's better to use comprehension than to use map

words = [word.upper() for word in text.split(" ")]
print(words)

# Using map to do the same thing
words_map = list(map(str.upper, text.split(" ")))
print(words_map)

for word in map(str.upper, text.split(" ")):
    print(word)

# Using re.split() to split the string with multiple arguments
for word_2 in map(str.upper, re.split(" |-", text)):
    print(word_2)
# Study more about this!!! https://www.codegrepper.com/code-examples/python/can+we+pass+multiple+separators+in+.split%28%29+python