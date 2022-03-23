budget = int(input())
products = int(input())
total = 0
counter = 0
for product in range(products):
    product_type = input()
    if product_type == "hoodie":
        total = total + 30
    elif product_type == "keychain":
        total = total + 4
    elif product_type == "T-shirt":
        total = total + 20
    elif product_type == "flag":
        total = total + 15
    elif product_type == "sticker":
        total = total + 1
    counter += 1

if budget >= total:
    print(f"You bought {counter} items and left with {budget - total} lv.")
else:
    print(f"Not enough money, you need {total - budget} more lv.")
