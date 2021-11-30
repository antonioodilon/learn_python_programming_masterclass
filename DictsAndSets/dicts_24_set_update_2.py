from dicts_21_remove_method import adverse_interactions

meds_to_watch = set()

meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')

# This code is more efficient than the one in dicts_24_set_update