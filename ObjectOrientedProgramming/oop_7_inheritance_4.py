from oop_7_inheritance_3 import Enemy, Drow

drow_1 = Drow("Masoj", "Hun'ett")  # Since we didn't specify any values, the default ones are used
print(drow_1)

print("-" * 80)

drow_2 = Drow("Viconia", "DeVir")
print(drow_2)

print("-" * 80)

drow_3 = Drow("Dinin", "Do'Urden")
print(drow_3)
drow_3.take_damage(15)
print(drow_3)

print("-" * 80)

drow_3.battle_cry_lolth()
drow_1.battle_cry_lolth()
drow_2.battle_cry_lolth()

print("-" * 80)

another_enemy = Enemy("Sarevok")
another_enemy.battle_cry_lolth()  # Since the superclass Enemy has no attribute
# battle_cry_lolth(), this produces an error