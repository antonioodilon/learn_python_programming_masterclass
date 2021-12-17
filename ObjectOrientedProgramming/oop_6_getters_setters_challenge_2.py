from oop_6_getters_setters_challenge import Player

antonio = Player("Antonio", level=1, score=0)
# print("Player information => Name: {0} ; Lives: {1} ; Level: {2} ; Score: {3}"
#       .format(antonio.name, antonio.lives, antonio.level, antonio.score))
# antonio.lives -= 1  # Removing 1 life from antonio. But lives cannot be negative
# print(antonio.lives)

print("-" * 80)

antonio.level -= 1
print(antonio.level)
print(antonio.score)

print("-" * 80)

print(antonio.level)
print(antonio.score)

print("-" * 80)

antonio.level = 5
print(antonio.level)
print(antonio.score)

print("-" * 80)

antonio.level += 10
print(antonio.level)
print(antonio.score)

print("-" * 80)

print(antonio)