# Use a for loop to multiply 5 by 8 like an early computer, by adding 5
# to 5 8 times.

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    # Remember to put "for i in range of the multiplier" here. That is,
    # for each of the 8 numbers, adding 5 to 0, 5 to 5,
    # 10 to 5 etc
    answer += number
    print(answer)