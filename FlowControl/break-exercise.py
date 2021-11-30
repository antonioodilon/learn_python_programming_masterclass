# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
'''for i in range(0, 100, 7):
    print(i)
'''

i = 0
while i <= 101:
    i += 7
    print(i)
    if i % 11 == 0:
        break

print("-" * 80)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
#Remember! 0 is divisible by any number!