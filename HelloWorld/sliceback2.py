alphabet = "abcdefghijklmnopqrstuvwxyz"

#Using slices
#1) Produce the letters qpo
#2) Produce edcba
#3) Slice the string to produce the last 8 characters, in reverse order

backwards = alphabet[16:13:-1]
print(backwards)

backwards2 = alphabet[-10:-13:-1]
print(backwards2)

backwards3 = alphabet[4::-1]
print(backwards3)

backwards4 = alphabet[:-9:-1]
print(backwards4)

backwards5 = alphabet[-1:-9:-1]
print(backwards5)