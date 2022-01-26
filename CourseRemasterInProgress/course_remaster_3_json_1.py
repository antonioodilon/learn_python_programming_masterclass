import json

# Converting our list of lists to a list of tuples in a practical way: on the
# top select Edit -> Find -> Replace, and replace the characters you don't
# want [] with the ones you want (). First opening square brackets [ -> ( ,
# and then closing square brackets ] -> )
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

with open('test_file_json_2.json', 'w', encoding='utf-8') as test_json_2:
    json.dump(languages, test_json_2)
    
with open('test_file_json_2.json', 'r') as test_json_2:
    data = json.load(test_json_2)

# Many programming languages don't have tuples, and JSON files are supposed
# to be able to be read by any language. Hence, in the output and in the JSON
# file we see a list of lists again instead of a list of tuples

# The types of data one can get from JSON:
# https://docs.python.org/3/library/json.html#encoders-and-decoders

# Use JSON when you want to store or transmit data in a format that other
# systems can use.

# JSON isn't good for storing your program's data, if you need to preserve
# the exact type.

# One of the good things about JSON is that its size is often many times
# smaller than other formats (such as XML, for instance), which means that
# this can be important when you want a web page to load quickly without
# having to wait while a large amount of data is downloaded.

print(data)
print(data[3])
print(type(data[3]))