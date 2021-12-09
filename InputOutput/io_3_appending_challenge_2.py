with open("fantasy characters2.txt", "a") as fantasy_appended:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>3} times {1} equals {2}".format(i, j, i * j),
                  file=fantasy_appended)
        print("-"*30, file=fantasy_appended)