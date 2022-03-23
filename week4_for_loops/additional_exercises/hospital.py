days = int(input())
doctors = 7
seen_patients = 0
unseen_patients = 0
patients_left = 0
patients_to_see = 0
patients_able_to_be_seen = 0

for day in range(1, days + 1):
    patients_number = int(input())
    if day in range(3, days + 1, 3):
        if seen_patients < unseen_patients:
            doctors = doctors + 1
    if patients_number <= doctors:
        seen_patients = seen_patients + patients_number
    else:
        patients_able_to_be_seen = doctors
        seen_patients = seen_patients + doctors
        patients_left = patients_number - doctors
        unseen_patients = unseen_patients + patients_left

print(f"Treated patients: {seen_patients}.")
print(f"Untreated patients: {unseen_patients}.")
