budget = float(input())
extras_number = int(input())
price_clothes = float(input())

decors = budget * 0.1
clothes_price = extras_number * price_clothes

if extras_number > 150:
    clothes_price = clothes_price - clothes_price * 0.1

total_price = decors + clothes_price
money_left = budget - total_price

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(total_price - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget - total_price):.2f} leva left.")

