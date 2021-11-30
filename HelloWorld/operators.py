a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # The result will produce a float
print(a // b)   # This is integer division
print(a % b)    # The remainder of the division of a and b

print()

for i in range(1, 4):
    print(i)

print()

for i in range(1, a // b):
    print(i)

print()

'''
for i in range(1, a / b):
    print(i)
    # This will produce an error because Python expects an integer, not a float
'''

# i, a and b are not expressions. They are bound to values, which in turn are expressions.

i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

bun_price = 2.40
money = 15
print(int(money // bun_price))

# In math multiplication and division take precedence. Same in Python:
print(a + b / 3 - 4 * 12)
print(a + (b / 3) - 4 * 12)
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

#We can also use variables:
c = a + b
d = c / 3
e = d - 4
f = e * 12
print(f)
# Or:
print (e * 12)