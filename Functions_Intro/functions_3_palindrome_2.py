def is_palindrome(string):
    # string = input("Please enter a word to check if it is a palindrome: ")
    if string[::-1].casefold() == string.casefold():
        print("'{}' is a palindrome".format(string))
    else:
        print("'{}' is not a palindrome".format(string))
    # return string[::-1].casefold() == string.casefold()


user_input = input("Please enter a word to check if it is a palindrome: ")
is_palindrome(user_input)


# def is_palindrome(string):
#     # user_word = string[::-1]
#     # return user_word == string
#     return string[::-1].casefold() == string.casefold()  # More concise code
#
#
# user_input = input("Please enter a word to check if it is a palindrome: ")
#
# if is_palindrome(user_input):
#     print("'{}' is a palindrome".format(user_input))
# else:
#     print("'{}' is not a palindrome".format(user_input))