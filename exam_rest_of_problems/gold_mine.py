locations = int(input())

for location in range(locations):
    expected_gold_per_day = float(input())
    days_per_location = int(input())
    total_per_location = 0
    average_per_location = 0
    for day in range(days_per_location):
        gold_mined = float(input())
        total_per_location += gold_mined
    average_per_location = total_per_location / days_per_location
    if average_per_location >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {average_per_location:.2f}.")
    else:
        diff = expected_gold_per_day - average_per_location
        print(f"You need {diff:.2f} gold.")
