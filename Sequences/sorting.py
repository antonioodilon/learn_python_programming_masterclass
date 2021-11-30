pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
# Sorting in alphabetical order

print(letters)

numbers = [4.5, 7.64, 3.14, 2.7807, 10.723, 10.8920]
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)
# sorted() creates a new list, while list.sort() modifies the list in place

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
# With key=str.casefold T (capital T) no longer appears in the beginning
# of the output
print(missing_letter)

print()

names =["Christina",
        "Zendaya",
        "paul",
        "duncan",
        "Gurney",
        "anthony",
        "Dynaehir"
        ]
print(names)
names.sort() # Case-sensitive sorting
print(names)
names.sort(key=str.casefold) #Case-insensitive sorting
print(names)