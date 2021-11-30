def sum_eo(n, t):
    while True:
        n = int(input("Please enter a positive number: "))
        t = input("Now enter a letter of the alphabet: ")
        for i in range(0, n):
            if t == "e":
                start = 0
            elif t == "o":
                start = 1
            else:
                return - 1
        return sum(range(start, n, 2))


user_choice = sum_eo("", "")
print(user_choice)

        #     if t == "e":
        #         while i % 2 == 0:
        #             print(sum(range(0, n)))
        #     if t == "o":
        #         while i % 2 != 0:
        #             sum_i = i + i
        #             print(sum_i)
        #             break
        #     # else:
            #     print("a")


# for i in range(0, 10):
#     if i % 2 != 0:
#         print(i)