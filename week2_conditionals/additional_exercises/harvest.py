from math import floor, ceil

x = int(input())
y = float(input())
z = int(input())
n = int(input())

grapes_total = x * y
wine = (grapes_total * 0.4) / 2.5

if wine >= z:
    remaining = wine - z
    remaining_per_person = remaining / n
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(remaining)} liters left -> "
          f"{ceil(remaining_per_person)} liters per person.")

else:
    needed = z - wine
    print(f"It will be a tough winter! More {floor(needed)} liters wine needed.")

