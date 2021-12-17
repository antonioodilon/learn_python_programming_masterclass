from oop_6_getters_setters import Player

antonio = Player("Antonio")
print("Player information => Name: {0} ; Lives: {1} ; Level: {2} ; Score: {3}"
      .format(antonio.name, antonio.lives, antonio.level, antonio.score))
antonio.lives -= 1  # Removing 1 life from antonio. But lives cannot be negative
print(antonio.lives)

print("-" * 80)

antonio.lives -= 1
print(antonio)  # Notice that because of the __str__ in oop_6_getters_setters,
# we have a print statement instead of <oop_6_getters_setters.Player object at 0x000002675694CE20>

print("-" * 80)

antonio.lives -= 1
print(antonio)

print("-" * 80)

antonio.lives -= 1
print(antonio)

print("-" * 80)

antonio.lives = 9
print(antonio)

# Example of what a setter would look like:
    # antonio.get_name()
# Example of what a getter would look like:
    # antonio.set_score()