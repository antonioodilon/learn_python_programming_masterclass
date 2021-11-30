from dicts_21_remove_method import *
# Tim said that in the course we'll study in more detail why import * should
# generally be avoided

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny", ]

for patient in trial_patients:
    prescription = patients[patient]
    prescription.remove(warfarin)  # remove() is more appropriate here because
    # it raises an error
    prescription.add(edoxaban)  # Removing warfarin and adding edoxaban instead
    print(patient, prescription)


# The more Pythonic way to deal with this is why try/except, which we'll
# learn about later:
# for patient in trial_patients:
#     prescription = patients[patient]
#     try:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     except KeyError:
#         print(f"Patient {patient} is not taking Warfarin. Please remove "
#               f"{patient} from the trial")
#     print(patient, prescription)


# With this code we are in danger of killing Kenny because he wasn't prescribed
# Warfarin in the first place:
# for patient in trial_patients:
#     prescription = patients[patient]
#     prescription.discard(warfarin)
#     prescription.add(edoxaban)  # Removing warfarin and adding edoxaban instead
#     print(patient, prescription)


# This method isn't ideal either, because with very large groups, iterating
# with an if/else block may take too long.
# for patient in trial_patients:
#     prescription = patients[patient]
#     if warfarin in prescription:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     else:
#         print(f"Patient {patient} is not taking Warfarin. Please remove "
#               f"{patient} from the trial")
#     print(patient, prescription)