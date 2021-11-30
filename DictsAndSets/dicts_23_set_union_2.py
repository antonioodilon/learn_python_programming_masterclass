from dicts_21_remove_method import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction -> Produces the same result

print(sorted(meds_to_watch))