# Tim Buchalka's solution:
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # To check if the string is indeed being printed correctly
    return string[::-1].casefold() == string.casefold()


user_input2 = input("Please enter a sentence to check if it is a "
                    "palindrome (Tim Buchalka's solution): ")

if palindrome_sentence(user_input2):
    print("'{}' is a palindrome (Tim Buchalka's solution)"
          .format(user_input2))
else:
    print("'{}' is not a palindrome (Tim Buchalka's solution)"
          .format(user_input2))