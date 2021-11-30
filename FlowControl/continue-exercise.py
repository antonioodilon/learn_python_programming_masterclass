#Write a program to print out all the numbers from 0 to 20 that AREN'T divisible by 3 or 5
#Zero is divisible by everything (zero shouldn't appear in the output)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)