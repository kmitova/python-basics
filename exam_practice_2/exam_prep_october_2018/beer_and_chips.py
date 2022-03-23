from math import ceil

name = input()
budget = float(input())
beer_bottles = int(input())
chips_packs = int(input())

beer_price = 1.2 * beer_bottles
chips_price_one_pack = beer_price * 0.45
chips_price = ceil(chips_price_one_pack * chips_packs)
total = beer_price + chips_price

if total <= budget:
    left = budget - total
    print(f"{name} bought a snack and has {left:.2f} leva left.")
else:
    needed = total - budget
    print(f"{name} needs {needed:.2f} more leva!")

