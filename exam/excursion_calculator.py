people = int(input())
season = input()
price = 0

if season == "spring":
    if people <= 5:
        price = 50
    else:
        price = 48
elif season == "summer":
    if people <= 5:
        price = 48.5
    else:
        price = 45
elif season == "autumn":
    if people <= 5:
        price = 60
    else:
        price = 49.5
elif season == "winter":
    if people <= 5:
        price = 86
    else:
        price = 85

total = price * people
if season == "summer":
    total = total - total * 0.15
elif season == "winter":
    total = total + total * 0.08

print(f"{total:.2f} leva.")
