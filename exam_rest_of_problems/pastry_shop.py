dish = input()
number = int(input())
day = int(input())
price = 0

if day in range(1, 15 + 1):
    if dish == "Cake":
        price = 24
    elif dish == "Souffle":
        price = 6.66
    elif dish == "Baklava":
        price = 12.6
else:
    if dish == "Cake":
        price = 28.7
    elif dish == "Souffle":
        price = 9.8
    elif dish == "Baklava":
        price = 16.98

total = price * number
if day in range(1, 22 + 1):
    if 100 <= total <= 200:
        total = total - total * 0.15
    elif total > 200:
        total = total - total * 0.25

if day in range(1, 15 + 1):
    total = total - total * 0.1

print(f"{total:.2f}")
