vip_ticket = 499.99
normal_ticket = 249.99
tickets = 0
transport = 0
price = 0
remaining = 0
total = 0
budget = float(input())
category = input()
people_number = int(input())

if 1 <= people_number <= 4:
    transport = budget * 0.75
elif 5 <= people_number <= 9:
    transport = budget * 0.60
elif 10 <= people_number <= 24:
    transport = budget * 0.50
elif 25 <= people_number <= 49:
    transport = budget * 0.40
elif people_number >= 50:
    transport = budget * 0.25

remaining = budget - transport

if category == "Normal":
    total = 249.99 * people_number
elif category == "VIP":
    total = 499.99 * people_number

if total <= remaining:
    money_left = remaining - total
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = total - remaining
    print(f"Not enough money! You need {money_needed:.2f} leva.")
