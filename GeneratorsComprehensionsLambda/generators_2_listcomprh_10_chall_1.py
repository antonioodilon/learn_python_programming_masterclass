# Challenge 1: Use the conditional expression to produce a list with the
# fizzbuzz results
fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz"
if x % 5 == 0 else str(x) for x in range(1, 51)]

print(fizzbuzz)
