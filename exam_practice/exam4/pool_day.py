from math import ceil

people = int(input())
entry_fee = float(input())
chair_fee = float(input())
umbrella_fee = float(input())

entry_fee_total = entry_fee * people
people_with_chairs = ceil(people * 0.75)
chairs = chair_fee * people_with_chairs
people_with_umbrellas = ceil(people * 0.5)
umbrellas = umbrella_fee * people_with_umbrellas

total = entry_fee_total + chairs + umbrellas
print(f"{total:.2f} lv.")
