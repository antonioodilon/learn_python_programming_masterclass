def remainder(x, y):
    result = x % y
    return result


answer = remainder(20, 3)
print(answer)


def multiply_divide(v, w, z):
    result = (v * w)/z
    return result


answer2 = multiply_divide(7.2, 5, 3)
print(answer2)

print()

for val in range(1, 10):
    divide = multiply_divide(30, 63, val)
    print(divide)