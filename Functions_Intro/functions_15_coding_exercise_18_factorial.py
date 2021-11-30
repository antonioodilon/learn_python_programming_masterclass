def factorial(number: int) -> int:
    """
    Return number! 0! is, by convention, 1.
    :param number: `int`
    :return: `int`
    """
    if number <= 1:
        return 1

    result = 2
    for x in range(3, number + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))


# Failed attempts below:
# def factorial(user_input):
#     for i in range(0, 36):
#         i += 1
#         return i
#
#
# user_answer = factorial()
# print(user_answer)

"Try to improve this one below!"
# for i in range(0, 36):
#     i += 1
#     number_now = i
#     # range_before = len(range(1, i + 1))
#     for number in range(1, i + 1):
#         print(i * number[1:i+1])

    #result = number_now * range_before
    # print(number_now)
    # print(range_before)

    # number_before = i - 1
    # result = i * number_before
    # print(result)


# list_numbers = [range(0,36)]
#
# for number in list_numbers:
#     print(number)