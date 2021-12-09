times_table = [
    "1 times 2 is 2",
    "2 times 2 is 4",
    "3 times 2 is 6",
    "4 times 2 is 8",
]

with open("fantasy characters.txt", "a") as fantasy_appended:
    for times in times_table[1:]:
        times[0].rjust(20)
        print(times, file=fantasy_appended)

print(fantasy_appended)

with open("fantasy characters.txt", "r") as fantasy_read:
    info = fantasy_read.readline()
    while info:
        print(info, end="")
        info = fantasy_read.readline()