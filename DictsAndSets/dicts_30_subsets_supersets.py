fantasy_universes = {
    "The Lord of the Rings",
    "Forgotten Realms",
    "Foundation",
    "Dune",
    "The Witcher",
    "Castlevania",
    "Star Wars",
    "Star Trek",
    "Mass Effect",
    "Dragon Age",
}

sci_fi_universes = {
    "Foundation",
    "Dune",
    "Star Wars",
    "Star Trek",
    "Mass Effect",
}

sword_sorcery_universes = {
    "The Lord of the Rings",
    "Forgotten Realms",
    "The Witcher",
    "Castlevania",
    "Dragon Age",
}

medieval_universes = {
    "Forgotten Realms",
    "The Witcher",
    "Castlevania",
    "Dragon Age",
    "The Lord of the Rings",
}

more_med_universes = {
    "The Witcher",
    "Forgotten Realms",
    "Sinbad",
    "Dragon Age",
    "Castlevania",
}

print(f"sci_fi_universes has no items in common with sword_sorcery_universes: "
      f"{sci_fi_universes.isdisjoint(sword_sorcery_universes)}")
# isdisjoint() method checks if a set has no items in common with another set

print(fantasy_universes <= sword_sorcery_universes)  # False. fantasy_universes
# isn't a subset of sword_sorcery_universes
print(sword_sorcery_universes < fantasy_universes)  # True. sword_sorcery_universes
# is a proper subset of fantasy_universes. This means that all items of the
# former also exist in the latter.

print(f"fantasy_universes is a superset of sword_sorcery_universes: "
      f"{fantasy_universes.issuperset(sword_sorcery_universes)}")
print(f"sword_sorcery_universes: is a subset of fantasy_universes:"
      f"{sword_sorcery_universes.issubset(fantasy_universes)}")

print(f"fantasy_universes is a subset of sword_sorcery_universes: "
      f"{fantasy_universes.issubset(sword_sorcery_universes)}")
print(f"sword_sorcery_universes is a superset of fantasy_universes:"
      f"{sword_sorcery_universes.issuperset(fantasy_universes)}")

print("-"*80)

print(medieval_universes == sword_sorcery_universes)
print(medieval_universes <= sword_sorcery_universes)
print(medieval_universes < sword_sorcery_universes)
# medieval_universes is a subset, but not a proper subset of sword_sorcery_universes

print("-"*80)

print(more_med_universes <= medieval_universes)
print(more_med_universes < medieval_universes)
# because of "Conan", more_med_universes is neither a subset nor a proper
# subset of medieval_universes