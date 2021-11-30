generated_list = ['9', ' ',
                  '2', '1', '4', ' ',
                  '3', '6', '8', ' ',
                  '8', '0', '7', ' ',
                  '6', '2', '7', ' ',
                  '7', '2', '4', ' ',
                  '4', '6', '1', ' ',
                  '1', '3', '7',
                  ]
print(generated_list)

# Important! My problem was that I thought the ' ' would produce an error
# when being converted to int

numbers = "".join(generated_list)
print(numbers)

numbers_list = numbers.split()
print(numbers_list)

# Method 1:
generated_list2 = []

for number in numbers_list:
    # int(number)
    generated_list2.append(int(number))

print(generated_list2)

# Method 2:
print(numbers_list) # Checking if the values are still indeed strings

for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])

print(numbers_list)
'''
separators = generated_list[1::4]
print(separators)

new_list = []
int_list = []

for char in generated_list:
    if char not in separators:
        int_numbers = map(int, char)
        new_list.append(int_numbers)
        int_list = list(new_list)

print(int_list)
'''


'''
numbers = "".join(generated_list).split(" ")
print(numbers)

int_numbers = map(int, numbers)
print(int_numbers)

int_list = list(int_numbers)
print(int_list)
'''

# for number in numbers:
#     int(number)
#     if isinstance(number, int):
#         print(number)
#
# print(numbers)

# separators = generated_list[1::4]
# print(separators)
#
# print(generated_list)
#
# numbers_list = []
#
# for char in generated_list:
#     if char not in separators:
#         int(char)
#         print(char)
#         char = "".join().split(char)
#         numbers_list.append(char)
#
# print(numbers_list)
# # print(type(numbers_list))
#
# numbers_list = "".join(for char in generated_list: if char not in separators: int(char) else)
# print(numbers_list)

# for char in generated_list:
#     if char == int:

# numbers4_list = "".join(char if char == int else " " for char in generated_list).split(" ")
# print(numbers4_list)