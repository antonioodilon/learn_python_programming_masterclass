alphabet = "abcdefghijklmnopqrstuvwxyz"
backwards = alphabet[25::-1] #Includes the character at index 0
print(backwards)

backwards2 = alphabet[25:0:-1] #Doesn't include the character at index 0
print(backwards2)

backwards3 = alphabet[25:1:-3]
print(backwards3)

backwards4 = alphabet[::-1] #We can omit the start value
print(backwards4)

backwards5 = alphabet[25:-1:-1] #No output because the second value, -1, is z,
                                # which comes right after a, on index 0
print(backwards5)

backwards6 = alphabet[25:-4:-1] #zyx
print(backwards6)