# Reviewing some methods from dicts, lists, sets and tuples

my_dict = {
    "Antonio": 1,
    "Maria": 2,
    "Luíza": 3,
    "Clara": 4,
}

my_list = []
my_list_2 = []

for key, value in my_dict.items():
    print(key, value)
    my_list.append(key)
    my_list_2.append(value)

print(my_list)
print(my_list_2)

my_list.extend(my_list_2)
print(my_list)

x = zip(my_list, my_list_2)
print(x)

# y = list(x)
# print(y)

z = dict(x)  # Now z = my_dict again
print(z)