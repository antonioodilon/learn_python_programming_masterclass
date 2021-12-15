def parabola(x):
    y = x * x
    return y


for i in range(-50, 51):
    j = parabola(i)
    print(i, j, sep=" : ")