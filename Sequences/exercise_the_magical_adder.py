# The user's input will be a string
# After that, separate the numbers in the string using a comma
# Convert each number to an int
# Perform the calculation of a + b - c

user_input = input("Please enter 3 numbers separated by commas ( , ) : ")
#user_input = "1,2,3"
user_input_modified = user_input.split(",")

for index in range(len(user_input_modified)):
    user_input_modified[index] = int(user_input_modified[index])

print(user_input_modified[0] + user_input_modified[1] -
      user_input_modified[2])

# Tim Buchalka's solution:
'''
# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
'''