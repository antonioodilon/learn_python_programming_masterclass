import funct_5_pytimezone_library_challenge
# We want to just import the code, not start and execute the code
# Therefore, we need to check the name attribute the code has and only
# execute it if it has the value of __main__

print(__name__)  # Output: __main__

# A useful way to iterate through a dictionary's keys:
g = sorted(globals())

for x in g:
    print(x)