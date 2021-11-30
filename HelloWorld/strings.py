print("Today is a good day to learn Python")
print('It is also a good day to weightlift')
print("Python's strings are easy to use")
print('You can even add "quotes" inside strings')
print("hello" + " world")

greeting = "Hello,"
name = "Antonio"
# name2 = input("Please enter your name ")
age = 30

print()

# print(greeting + " " + name2)
print(greeting + " " + name)
print(age)

print(type(greeting))
print(type(age))

# rebounding the variable age to a type string
'''
age = "30"
print(age)
print(type(age))
'''

age_str = "30"
print(age_str)
print(type(age_str))

# Cannot concatenate str and int:
print(name + " is " + age + " years old.")
# Transforming age into string: str(age)