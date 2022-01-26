import json

# Below, a list of the languages that influenced Python, and the year they
# were first used
languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

with open('test_file_json.json', 'w', encoding='utf-8') as test_json:
    json.dump(languages, test_json)  # .dump() serializes the object in JSON
    # format

# Now reading the file back again:
with open('test_file_json.json', 'r') as test_json:
    data = json.load(test_json)

print(data)
print(data[3])
print(type(data[3]))
