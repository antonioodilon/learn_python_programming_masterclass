def sum_numbers(*args: float) -> float:
    """
    The function calculates the sum of all numbers passed as arguments in
    a variable number of arguments (a `tuple`).
    :param args: `float`. Whatever is the amount of numbers the user passes
    as arguments when s/he calls the function.
    :return: `float`. The sum of all numbers passed as arguments.
    """
    # print(*args)
    start = args[0]
    for values in args[1:]:
        start += values
    return start


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
print(sum_numbers(5, 10, 15, 20, 25))


# result1 = dividend / divisor
# result1 += (sum_arg1, sum_arg2, sum_arg3, sum_argn)
# multiplier *= result1
def calculate_numbers(dividend: float, divisor: float, *sum_args: float,
                      multiplier: float) -> float:
    """
    Calculates a series of numbers that the user passes as arguments. Sums
    the two first arguments (dividend and divisor), then sums its result
    with all the `float` values inside the *sum_args `tuple`. Its result is then
    multiplied by the key multiplier and returned to the global scope.
    :param dividend: `float`
    :param divisor: `float`
    :param `float`
    :param multiplier: `float`
    :return: `float`
    """
    result = dividend / divisor
    for values in sum_args:
        result += values
    result *= multiplier
    return result


print(calculate_numbers(9, 3, 1, 2, 3, 4, multiplier=3))
print(calculate_numbers(4, 2, 1, 2, 3, 4, multiplier=5))