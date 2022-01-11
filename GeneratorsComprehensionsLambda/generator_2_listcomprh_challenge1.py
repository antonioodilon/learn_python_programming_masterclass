# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)

# type your solution here:
output_2 = [len(x) for x in text.split()]
print(output_2)


# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

# type the corresponding comprehension here:
output_3 = [(x, len(x)) for x in text.split()]
print(output_3)

# It could be useful to use a set comprehension sometimes, given that sets
# work with unique items, and the user could type a phrase that has duplicate
# words:
output_set = {(x, len(x)) for x in text.split()}
print(output_set, type(output_set))

# Trying to remove the non-alphanumberic characters. This was my first attempt:
output_set_alnum = {"".join(x for x in text.split() if x.isalnum())}
print(output_set_alnum)
# Tim said that we will fix this when we look at nested comprehensions later