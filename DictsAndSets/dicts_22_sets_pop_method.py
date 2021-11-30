from dicts_21_remove_method import patients

# In sets, the pop() method removes random items from them. Very useful
# when you don't care about the order the items are removed, as long as
# they are removed

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny", }

for patient in patients:
    print(f"{patient}: {patients[patient]}")

print("-"*80)

# This code ensures that we don't produce prescriptions for the same patient
# again:
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)