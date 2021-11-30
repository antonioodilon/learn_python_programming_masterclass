# import copy

people = {
    "Grandsons": {
        "Antonio": 1,
        "Bruno": 3,
        "Gabriel": 2,
    },
    "Granddaughters": {
        "Maria": 3,
        "Juno": 4,
        "Fernanda": 0,
        "Marília": 1,
    },
    "Sons": {
        "Adriano": 1,
        "André": 2,
        "João": 5,
    },
    "Daughters": {
        "Antoinette": 1,
        "Júlia": 3,
    },
}


def my_deepcopy(d: dict) -> dict:
    user_dict = {}
    for key, value in d.items():
        user_dict = d.copy()
        for key1, value1 in value.items():
            # user_dict[key1] = value1
            print(key1, value1)
    return user_dict


    # user_dict = d.copy()
    # for key, value in d.items():
    #     for key1, value1 in value:
    #         user_dict[key][value][key1] = value1
    # return user_dict


people["Sons"]["Tonico"] = 1
print(people)
my_deepcopy(people)

# print(people)
# citizens = people.copy()
# print(citizens)
#
# print("-"*100)
#
# citizens["Sons"]["Tonico"] = 2
#
# print(people["Sons"])
# print(citizens["Sons"])