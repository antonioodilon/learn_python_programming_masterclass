from oop_7_inheritance_3 import Enemy, Drow, Druchii

# drow_4 = Drow("Malice", "Do'Urden")
# print(drow_4)
# drow_4.take_damage(10)
# print(drow_4)
#
# print("-" * 80)
#
# druchii_1 = Druchii("Malekith", "Naggarond")
# druchii_1.take_damage(15)
# print(druchii_1)
#
# print("-" * 80)

druchii_2 = Druchii("Malus", "Har Graef")
# druchii_2.take_damage(10)
print(druchii_2)

# while True:
#     druchii_2.take_damage(1)
#     print(druchii_2)
#     if druchii_2.lives == 0:
#         break

# Code that Tim wrote:
while druchii_2.alive:
    druchii_2.take_damage(1)
    print(druchii_2)