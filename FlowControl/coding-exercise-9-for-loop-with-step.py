for i in range(0, 100):
    if i % 7 == 0:
        print("The number {0} is divisible by 7".format(i))

print("-" * 80)

for i in range(101)[::7]:
    print("The number {0} is divisible by 7".format(i))