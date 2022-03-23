baklava_price_kg = float(input())
muffins_price_kg = float(input())
stolen_kg = float(input())
candy_kg = float(input())
cookies_kg = int(input())

stolen_kg_price = baklava_price_kg + baklava_price_kg * 0.6
stolen_price = stolen_kg_price * stolen_kg
candy_kg_price = muffins_price_kg + muffins_price_kg * 0.8
candy_price = candy_kg_price * candy_kg
cookies_price = cookies_kg * 7.5
total = stolen_price + candy_price + cookies_price
print(f"{total:.2f}")
