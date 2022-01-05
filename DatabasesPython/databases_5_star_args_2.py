# **kwargs refers to a variable number of keywords
# kw = key words
# * (1 asterisk) unpacks a tuple or list
# ** (2 asterisks) unpacks a dictionary

def print_backwards(*args, file=None):
    for element in args[::-1]:
        print(element[::-1], end=' ', file=file)


with open("databases_5_kwargs", "w") as databases_5_kwargs:
    print_backwards("The", "power", "of", "Chaos", "flows", "within", "me!",
                    file=databases_5_kwargs)


# With **kwargs the code that calls the function is free to add as many keyword
# arguments as print will accept, and we don't need to worry about what they
# are or what their default values are:

print("The power of Chaos", "flows", "within", "me!", sep='-')


# Providing a variable number of arguments with *args and a variable number
# of keywords with **kwargs
def print_backwards_kwargs(*args, **kwargs):
    print(kwargs)  # Notice that kwargs is a dictionary
    for element in args[::-1]:
        # My solution to the challenge in class 358 involved a try and except
        # block of code:
        try:
            print(element[::-1], end=' ', **kwargs)
        except TypeError:
            print(element[::-1], **kwargs)


with open("databases_5_kwargs_2", "w") as databases_5_kwargs_2:
    print_backwards_kwargs("The power of Chaos", "flows", "within", "me!",
                           end=' ', file=databases_5_kwargs_2)


# In the challenge one of Tim's solution was to remove the keyword 'end'
# from the kwargs dictionary:
def print_backwards_tim(*args, **kwargs):
    kwargs.pop('end', None)
    for element in args[::-1]:
        print(element[::-1], end=' ', **kwargs)


print(end='\n')

print_backwards_tim("The power of Chaos", "flows", "within", "me!", end='\n')
print("Another string")

print("-" * 80)


# Now let's make sure that the end and sep keywords behave the way we want
# them to behave. Pay attention that changing the behaviour of the keywords
# can create problems, which is exactly what happened and that we attempted
# to fix.
def print_backwards_2(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for element in args[:0:-1]:  # Changing the range. Since this print function
        # works backwards, we will start with the last element, then work
        # backwards up to, but not including, the first element
        print(element[::-1], end=sep_character, **kwargs)  # end=sep_character
        # means that we are forcing each element to be printed on the same line
        # by default, as a regular print function would do
    print(args[0][:0:-1], end=end_character, **kwargs)  # Since the first
    # element wasn't included, we will include it not and print it separately,
    # after the for loop ends
    # print(sep=end_character)  # We don't need this line anymore


print("-" * 80)
print("The power of Chaos", "flows", "within", "me!", end='', sep='\n!!\n')
print()
print_backwards_2("The power of Chaos", "flows", "within", "me!", end='',
                  sep='\n!!\n')

print('\n')
print("Lord", "Khorne,", "grant", "me", "your", "power!")
print("-" * 80)


# This is how Tim would have written the code above (however, we will still
# learn this technique, probably in the next section):
def better_backwards(*args, **kwargs):
    sep_character = kwargs.pop('sep', '/')  # Tim used a space ' ' as the
    # default value, but I put a / just to confirm that the second argument
    # to .pop() is the value we are replacing the value of the dictionary
    # kwargs with
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


# Reviewing lists and dictionaries:

better_backwards("Lord", "Khorne,", "grant", "me", "your", "power!")

print("-" * 80)

a_list = ["Lord", "Khorne,", "grant", "me", "your", "power!"]
print(a_list)

removed_item_list = a_list.pop(3)  # Removing the item on index position 3
print("Item removed: ", removed_item_list)
print("Updated list: ", a_list)

print("-" * 80)

a_dict = {
    1: "Khorne",
    2: "Nurgle",
    3: "Tzeentch",
    4: "Slaanesh",
    5: "Hashut",
}
print(a_dict)

popped_value = list(a_dict.values()).pop(3)
print(popped_value)

print(a_dict)

# print(values_dict)
# print(type(values_dict))

# keys_a_dict = list(a_dict)
# print(keys_a_dict)
# print(type(keys_a_dict))
# remove_value_add_another = a_dict.pop(a_dict[3], "The Horned Rat")

# print(a_dict)

# remove_and_add_item_list = another_list.pop("Tzeentch", "Nurgle")
















