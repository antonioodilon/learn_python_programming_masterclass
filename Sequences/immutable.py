# Strings, booleans and others are immutable in Python

result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
another_result = result
print(id(result))
print(id(another_result))

print()

result1 = "Correct"
another_result1 = result1
print(id(result1))
print(id(another_result1))

result1 += "ish"
another_result1 = result1
print(id(result1))
print(id(another_result1))