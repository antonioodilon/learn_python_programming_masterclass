import timeit
import functools

numbers = [2, 4, 5, 10.5, 12.6, 25]


# Briefly reviewing how to write functions:
def sum_numbers(number_list: list) -> float:
    initial_value = 0
    for number in number_list:
        initial_value += number
    return initial_value


print(sum_numbers(numbers))

print("=" * 60)


def sum_values(x, y: bool):
    return x + y


numbers_2 = [10, 11, 15, 20, 23]

# functools.reduce() calculates the product between the first two numbers in
# an iterable, then again between the result and the next number and so on.
# It can be used with addition (which is kind of pointless, because the sum()
# function already takes care of that), multiplication etc
reduced_value = functools.reduce(sum_values, numbers_2)
print(reduced_value)
print(sum(numbers_2))

print("=" * 60)

numbers_3 = [2, 4, 6, 7, 10]


def multiply_values(x, y: bool):
    return x * y


def multiply_values_2(number_list: list) -> float:
    initial_value = 1
    for number in number_list:
        initial_value *= number
    return initial_value


reduced_value_2 = functools.reduce(multiply_values, numbers_3)
print(reduced_value_2)
print(multiply_values_2(numbers_3))