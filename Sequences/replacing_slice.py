computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat",
                  "stabilizer"
                  ]
print(computer_parts)
computer_parts.append("motherboard")
print(computer_parts)

'''
computer_parts[3] = "trackball" #   changing item in index position 3 to
# trackball
print(computer_parts)
'''

'''
computer_parts[3:5] = "trackball" # since strings are iterables, this replaces
# items at index positions 3 and 5-1 with each of the characters in the word
# "trackball"
print(computer_parts)
'''

computer_parts[3:5] = ["trackball"]  # to fix this problem, we turn trackball
# into a list by using []
print(computer_parts)

print(list(enumerate(computer_parts)))
