numbers = set(range(31))
print(numbers)

numbers.clear() # Removing all the items from a set.
print(numbers)

other_numbers = set(range(21))
print(other_numbers)

other_numbers.remove(5)
other_numbers.discard(15)
print(other_numbers)

print("-"*80)
other_numbers.discard(35)
print(other_numbers)
other_numbers.remove(30)  # remove() raises an error when the item is not
# present in the set
print(other_numbers)