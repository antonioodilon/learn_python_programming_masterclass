from oop_7_inheritance import Enemy, Drow

basic_enemy = Enemy("Basic enemy", 15, 1)
print(basic_enemy)

basic_enemy.take_damage(8)
print(basic_enemy)

basic_enemy.take_damage(7)
print(basic_enemy)

basic_enemy.take_damage(5)
print(basic_enemy)

print("-" * 80)

drow_1 = Drow()  # Since we didn't specify any values, the default ones are used
print(drow_1)

drow_2 = Drow("Briza", 15)
print(drow_2)

drow_3 = Drow("Dinin", 18, 2)
print(drow_3)
drow_3.take_damage(15)
print(drow_3)