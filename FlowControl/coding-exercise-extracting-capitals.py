statement = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"
extracted_capitals = ""

for char in statement:
    if char.isupper():
        extracted_capitals = extracted_capitals + char

print(extracted_capitals)