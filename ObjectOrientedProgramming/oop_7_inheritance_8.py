from oop_7_inheritance_challenge import Enemy, Drow, Druchii, DruchiiMonarch, \
    DruchiiMonarch2

druchii_1 = Druchii("Malus", "Har Graef")
print(druchii_1)

druchii_monarch_1 = DruchiiMonarch("Malekith", "Naggarond")
print(druchii_monarch_1)

druchii_monarch_2 = DruchiiMonarch2("Morathi", "Naggarond")
print(druchii_monarch_2)

# Code that Tim wrote:
while druchii_1._alive:
    druchii_1.take_damage(1)

print(druchii_1)

# Now, after modifying take_damage(), we can remove the if not line below:
# while druchii_1.alive:
#     if not druchii_1.parry():
#         druchii_1.take_damage(1)
#         print(druchii_1)

print("-" * 80)

while druchii_monarch_1._alive:
    druchii_monarch_1.take_damage(1)
    print(druchii_monarch_1)

print("-" * 80)

while druchii_monarch_2._alive:
    druchii_monarch_2.take_damage(16)
    print(druchii_monarch_2)