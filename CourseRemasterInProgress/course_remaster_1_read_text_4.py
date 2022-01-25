input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        row_data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = row_data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        # print(row_data)
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        print(country_dict)
        countries[country.casefold()] = country_dict

print(countries)

# Challenge: get a country name for the user, then display the capital city
# for the chosen country:
for key, value in countries.items():
    for sub_key, sub_value in value.items():
        if sub_key == 'capital':
            print(key, sub_value)

print("=" * 80)

# Doing the same thing, but using comprehension
for key, value in countries.items():
    name_capital = [(key, sub_value) for sub_key, sub_value in value.items()
                    if sub_key == 'capital']
    print(name_capital)

# Another solution:
chosen_country = input("Please enter a country's name ").casefold()
if chosen_country in countries:
    for key, value in countries[chosen_country].items():
        if key == 'capital':
            print(value)

# Tim's solution:
while True:
    chosen_country_2 = input("Please enter a country's name and I'll tell you "
                             "its capital.\nType 'quit' to leave the program ")
    country_key = chosen_country_2.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print("The capital of {0} is {1}".format(chosen_country_2, country_data['capital']))
    elif chosen_country_2 == 'quit':
        print("Ok, have a great day!")
        break
    else:
        print("Please type in a valid country")


# name_capital_country = [(key, sub_value) for sub_key, sub_value in value.items()
#                         for key, value in countries.items() if sub_key == 'capital']

# user_input = input("Please type the name of the country, and I'll tell you "
#                    "its capital: ")
# for key, value in countries.items():
#     for sub_key, sub_value in value.items():
#         if user_input == sub_key:
#             print(sub_key, sub_value)
            # print(key[value])
    # key = user_input
    # name_capital_2 = value.get(key)
    # name_capital = [(user_input, sub_value) for sub_key, sub_value in value.items()
    # if 'capital' == user_input[sub_key].values()]
                    # if sub_key == 'capital']
    # print(name_capital_2)