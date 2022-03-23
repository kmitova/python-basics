strawberries_price_kg = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price_kg = strawberries_price_kg / 2
oranges_price_kg = raspberries_price_kg - raspberries_price_kg * 0.4
bananas_price_kg = raspberries_price_kg - raspberries_price_kg * 0.8

strawberries_price = strawberries_quantity * strawberries_price_kg
bananas_price = bananas_price_kg * bananas_quantity
oranges_price = oranges_price_kg * oranges_quantity
raspberries_price = raspberries_price_kg * raspberries_quantity

price = strawberries_price + bananas_price + oranges_price + raspberries_price
print(f"{price:.2f}")
