from dicts_25_primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 51, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)

squares = set(squares_generator(100))
print(squares)

# Odd numbers that aren't primes:
print(odds.difference(primes))
# Using the operator:
print(odds - primes)

# Prime numbers that are not odds:
print(primes.difference(odds))
print(primes - odds)  # 2 is the only prime less than 50 that is in the output
# because 2 is even.