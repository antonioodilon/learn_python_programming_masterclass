from dicts_25_primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 51, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

# Printing the primes less than 100:
primes = set(primes_generator(100))
print(primes)

# Printing the squares less than 100:
squares = set(squares_generator(100))
print(squares)

# Intersection of the odds less than 50 and squares. That is, the odd numbers
# less than 50 that are also squares:
odds_squares = odds.intersection(squares)
print(odds_squares)