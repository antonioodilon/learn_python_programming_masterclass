def average(*args):
    print(type(args))  # args is the tuple
    # print(type(*args))  # This causes an error!
    print("args is", args)  # here we have the tuple
    print("*args is", *args)  # *args represents the unpacked tuple
    mean = 0
    for number in args:
        mean += number
    return mean / len(args)


print(average(4, 6, 8, 10))

print("-"*80)


# Solving the challenge from video 356: write a function called build_tuple
# which takes a variable number of arguments and returns a tuple with those
# arguments:
def build_tuple(*args):
    return args


nwn_tuple = build_tuple("Neverwinter", "Nights", "is", "a", "great", "game")
print(nwn_tuple)
print(type(nwn_tuple))

print("-"*80)


# Other challenges that Buchalka proposed are below.

# Challenge 1: Create a function that takes a variable number of words, and
# returns the average word length
def avrg_word_len(*args):
    # len_word = 0  # Useless!
    mean = 0
    for word in args:
        len_word = len(word)
        mean += len_word
    return mean / len(args)


words = avrg_word_len("Neverwinter", "Nights", "is", "a", "great", "game")
print(words)

print("-"*80)
"""
Articles that helped with solving this challenge:
https://www.kite.com/python/answers/how-to-iterate-through-a-list-of-tuples-in-python#:~:text=Use%20enumerate()%20to%20iterate,list%20of%20tuples%20in%20enumerate_object%20.
"""


# Challenge 2: Create a function that returns the smallest or largest of the
# numbers passed to it.
def largest(*args):
    maximum = args[0]
    for number in args:
        if number > maximum:
            maximum = number  # If the next number is greater than the maximum,
            # then maximum acquires the value of number
    return maximum
        # position_next_number = args.index(number) + 1
        # position_number = args.index(number)
        # if args[position_next_number] > args[position_number]:
        #     print(args[position_next_number])
        # else:
        #     print(args[position_number])
        # print(args.index(number))


numbers2 = largest(2, 10, 3, 40, 5, 1, 100, 56)
print(numbers2)
# We have the index of the number and the index of the position of the next
# number
print("-"*80)
"""
Articles that helped solve this challenge:
https://www.programiz.com/python-programming/methods/tuple/index
https://www.toppr.com/guides/computer-science/programming-with-python/tuples/tuple-indexing/
https://stackoverflow.com/questions/216972/what-does-it-mean-if-a-python-object-is-subscriptable-or-not
https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/
"""


# Challenge 3: A function to print all the words passed to it backwards, in
# reverse order. So the output will read correctly from right to left. Hint:
# We saw how to reverse a string using a slice of [::-1], and that can also
# be used with tuples.
# In my solution I decided to reverse the order of the letters in the words
# as well
def backwards(*args):
    a_tuple = ()
    print(type(a_tuple))
    for word in args:
        word_backwards = (word[::-1],)  # Transforming it into a tuple
        a_tuple += word_backwards  # Tuples can only be joined with other
        # tuples
    print(*a_tuple)
    for element in a_tuple:
        print(element)
    print("Finally, the solution to challenge is:\n", a_tuple[::-1])

    # First solution: append all the words in backwards to a list:
    # list_words = []
    # for word in args:
    #     list_words.append(word[::-1])
    # return list_words


backwards("Neverwinter", "Nights", "is", "a", "great", "game")

print("-"*80)
"""
Articles that helped solve this challenge:
https://stackoverflow.com/questions/16730339/python-add-item-to-the-tuple
https://stackoverflow.com/questions/47272460/python-tuple-unpacking-in-return-statement
https://www.pythontutorial.net/python-basics/python-unpacking-tuple/
https://www.tutorialspoint.com/unpacking-a-tuple-in-python
"""


# Challenge 4: Create a list, let's say you called it words. Print the list,
# but also print *words, to see that * can be used to unpack a list as well
# as a tuple.
# In my solution I called the list my_list, not words
def unpack_list(*args):
    my_list = []
    for element in args:
        my_list.append(element)
    print(my_list)
    print(*my_list)


unpack_list("I", "absolutely", "love", "Baldur's", "Gate")
