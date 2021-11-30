# Revisiting the code slicing2 from section HelloWorld

numbers = "3,464 575:686;797,808 919"
separators = numbers[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values])  #Printing a list with the values

print("-" * 60)

numbers2 = "900,210,36,8,62,7,461,137"
print(numbers2.split(","))

print("-" * 60)

generated_list = ['9', '0', '0', ' ',
                  '2', '1', '0', ' ',
                  '3', '6', ' ',
                  '8', ' ',
                  '6', '2', ' ',
                  '7', ' ',
                  '4', '6', '1', ' ',
                  '1', '3', '7',
                  ]

print(generated_list)

print("-" * 60)

numbers3 = "".join(generated_list)
print(numbers3)

print("-" * 60)

numbers3_list = numbers3.split(sep=" ")
print(numbers3_list)

print("-" * 60)

numbers4_list = "".join(generated_list).split(" ")
print(numbers4_list)