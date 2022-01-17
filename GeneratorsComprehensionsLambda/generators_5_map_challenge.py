import timeit

# The challenge is to check which approach is faster: map() or comprehension

text = "I shall be the high-handed slayer!"

chars_comp_timeit = """\
chars = [char.upper() for char in text]
print(chars)
"""

chars_map_timeit = """\
chars_map = list(map(str.upper, text))
print(chars_map)
"""

words_comp_timeit = """\
words = [word.upper() for word in text.split(" ")]
print(words)
"""

words_map_timeit = """\
words_map = list(map(str.upper, text.split(" ")))
print(words_map)
"""

# Remember: when passing a function as an argument to another function,
# DON'T USE PARENTHESES!
result_1 = timeit.timeit(chars_comp_timeit, globals=globals(), number=1000)
result_2 = timeit.timeit(chars_map_timeit, globals=globals(), number=1000)
result_3 = timeit.timeit(words_comp_timeit, globals=globals(), number=1000)
result_4 = timeit.timeit(words_map_timeit, globals=globals(), number=1000)

print("Result for chars using comprehension: {} \t".format(result_1))
print("Result for chars using map: {} \t".format(result_2))
print("Result for words using comprehension: {} \t".format(result_3))
print("Result for words using map: {} \t".format(result_4))
