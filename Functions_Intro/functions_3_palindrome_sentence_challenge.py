def is_palindrome(string):
    string = ''.join(char for char in string if char.isalnum())
    print(string)  # To check if the string is indeed being printed correctly
    if string[::-1].casefold() == string.casefold():
        print("'{}' is a palindrome".format(string))
    else:
        print("'{}' is not a palindrome".format(string))


# Tim Buchalka's solution (modified my me):
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # To check if the string is indeed being printed correctly
    if string[::-1].casefold() == string.casefold():
        print("'{}' is a palindrome (Tim Buchalka's solution)"
              .format(string))
    else:
        print("'{}' is not a palindrome (Tim Buchalka's solution)"
              .format(string))


user_input = input("Please enter a sentence to check if it is a "
                   "palindrome: ")
is_palindrome(user_input)


# Below are blocks of code from previous attempts:
# if, in the range of the string, there is a character that is not alphanumeric
# ignore it

# if not string[:].isalnum() and not string[::-1].isalnum():
#     pass

# for char in string:
#     if not char.isalnum():
#         continue

'''
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
'''

# for char in string:
#     if not char.isalnum():
#     #if any(not char.isalnum() for char in string):
#         pass