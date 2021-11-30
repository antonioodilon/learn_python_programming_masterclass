from dicts_13_copy_challenge_3 import my_deepcopy
import copy

dict_people = {
    "Antonio": ["de Odilon", ["Coder", "English teacher"]],
    "Antoinette": ["Madureira", ["Singer", "Professor"]],
}

copy1 = copy.deepcopy(dict_people)  # The deepcopy function goes all the
# way
copy2 = my_deepcopy(dict_people)    # The my_deepcopy function only goes one
# level down, and doesn't affect the entire dictionary

dict_people["Antonio"].append("Recife")
dict_people["Antoinette"].append("Natal")

dict_people["Antonio"][1].append("Teacher at NumberOne")
copy_antoinette = dict_people["Antoinette"]
copy_antoinette[1].append("Cashier at Banco do Nordeste")

copy3 = copy.deepcopy(dict_people)  # Since Python reads the code from top
# to bottom and from left to right, by the time it got to this line of code,
# all the previous information had been added to our dictionary

print(dict_people)  # dict_people with all the added information
print(copy1)    # a deepcopy that goes all the way down. Contains only the
# original dict_people declared on lines 4 to 7
print(copy2)    # my_deepcopy only goes down one level
print(copy3)    # a deepcopy with all the information so far, including
# what's written on lines 17 to 19, since Python reads code from top to bottom