month = input()
hours_spent = int(input())
people_in_the_group = int(input())
time_of_day = input()
price = 0

if month == "march":
    if time_of_day == "day":
        price = 10.5
    else:
        price = 8.4
elif month == "april":
    if time_of_day == "day":
        price = 10.5
    else:
        price = 8.4
elif month == "may":
    if time_of_day == "day":
        price = 10.5
    else:
        price = 8.4
if month == "june":
    if time_of_day == "day":
        price = 12.6
    else:
        price = 10.2
elif month == "july":
    if time_of_day == "day":
        price = 12.6
    else:
        price = 10.2
elif month == "august":
    if time_of_day == "day":
        price = 12.6
    else:
        price = 10.2

if people_in_the_group >= 4:
    price = price - price * 0.1

if hours_spent >= 5:
    price = price - price * 0.5

total = price * people_in_the_group * hours_spent

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total:.2f}")
