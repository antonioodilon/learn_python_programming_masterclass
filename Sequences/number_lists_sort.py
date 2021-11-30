# The sort() method doesn't create a new list. It rearranges the items in a list
# If you were to create a copy of the list, you could run out of memory

even = [2, 4, 6, 8, 10, 12]
odd = [1, 3, 5, 7, 9, 11]

even.extend(odd)
print(even)

even.sort()
print(even)
another_even = even

print(id(even))
print(id(another_even))
# Notice that the ids of even and another_even are the same

even.sort(reverse=True)
print(even)
print(another_even)