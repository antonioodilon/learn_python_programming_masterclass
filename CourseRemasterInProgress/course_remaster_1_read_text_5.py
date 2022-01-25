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
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict
print(countries)
        # code_lookup[code.casefold()] = country

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

# Antarctica doesn't have a capital city. A good way to practice more would be
# to print a message for a country like Antarctica that doesn't have a capital
# Identify the countries that don't have a value for their capital field.
# Write code to iterate over the dictionary and print the country name of any
# country without a capital.
