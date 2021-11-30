# See the codes in 3_palindrome_sentence_challenge
def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # To check if the string is indeed being printed correctly
    return is_palindrome(string)  # Calling is_palindrome() function from another
                            # function


user_input2 = input("Please enter a sentence to check if it is a "
                    "palindrome (Tim Buchalka's solution): ")

if palindrome_sentence(user_input2):
    print("'{}' is a palindrome (Tim Buchalka's solution)"
          .format(user_input2))
else:
    print("'{}' is not a palindrome (Tim Buchalka's solution)"
          .format(user_input2))