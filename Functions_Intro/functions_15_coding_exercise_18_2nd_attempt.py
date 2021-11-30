# for i in range(0, 36):
#     i += 1
#     # print(i)
#     for x in range(1, i + 1):
#         i *= x
#         print(i)

# IMPROVE!!

def factorial(x: int) -> int:
    if x <= 1:
        return 1
    base = 2
    for i in range(3, x + 1):
        base *= i
        #print(i, base)
    return base


for number in range(36):
    print(number, factorial(number))
