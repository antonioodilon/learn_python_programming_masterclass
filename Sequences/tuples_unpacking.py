a = b = c = d = e = f = 80
print(d)

x, y, z = 2, 4, 16
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 2, 4, 16
print(data)

x, y, z = data  #x, y and z are variables, each of them getting a value
# from the tuple "data"
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [3, 9, 81]
data_list.append(27)  # Since tuples are immutable, they can't be appended.
g, h, i = data_list
print(g)
print(h)
print(i)