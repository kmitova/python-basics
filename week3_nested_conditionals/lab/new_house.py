flower_type = input()
flowers_number = int(input())
budget = int(input())
price = 0
price_total = 0

if flower_type == "Roses":
    price = 5
    if flowers_number > 80:
        price_total = (price - price * 0.1) * flowers_number
    else:
        price_total = price * flowers_number
elif flower_type == "Dahlias":
    price = 3.80
    if flowers_number > 90:
        price_total = (price - price * 0.15) * flowers_number
    else:
        price_total = price * flowers_number
elif flower_type == "Tulips":
    price = 2.80
    if flowers_number > 80:
        price_total = (price - price * 0.15) * flowers_number
    else:
        price_total = price * flowers_number
elif flower_type == "Narcissus":
    price = 3
    if flowers_number < 120:
        price_total = (price + price * 0.15) * flowers_number
    else:
        price_total = price * flowers_number
elif flower_type == "Gladiolus":
    price = 2.50
    if flowers_number < 80:
        price_total = (price + price * 0.2) * flowers_number
    else:
        price_total = price * flowers_number

if budget - price_total >= 0:
    left_money = budget - price_total
    print(f"Hey, you have a great garden with {flowers_number} {flower_type} and {left_money:.2f} leva left.")
else:
    money_needed = price_total - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
