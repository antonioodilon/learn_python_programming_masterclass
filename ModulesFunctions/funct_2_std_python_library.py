import shelve
import random

"""
dir() is a powerful inbuilt function in Python3, which returns list of the
]attributes and methods of any object (say functions , modules, strings,
lists, dictionaries etc.) Syntax : dir({object})
"""
print(dir())

for m in dir(__builtins__):
    print(m)

print("-" * 80)

print(dir(shelve))
# Analyzing which methods the shelve module provides

print("-" * 80)

for obj in dir(shelve.Shelf):
    if obj[0] != "_":  # If the object doesn't start with an underscore _
        print(obj)

print("-" * 80)

help(shelve)  # To get more information about the shelve module

help(random.randint)  # Can also get help from individual functions