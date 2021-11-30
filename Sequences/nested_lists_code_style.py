empty_list = []
even = [2, 4, 6, 8, 10, 12]
odd = [1, 3, 5, 7, 9, 11]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for number in number_list:
        print(number)