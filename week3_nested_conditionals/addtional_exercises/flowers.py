chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
holiday_or_not = input()
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15

price = tulip_price * tulips_number + \
        chrysanthemum_number * chrysanthemum_price + roses_number * rose_price

if holiday_or_not == "Y":
    price = price + price * 0.15

if tulips_number > 7 and season == "Spring":
    price = price - price * 0.05
if roses_number >= 10 and season == "Winter":
    price = price - price * 0.1
if roses_number + chrysanthemum_number + tulips_number > 20:
    price = price - price * 0.2
    total_price_no_discount = tulip_price * tulips_number + chrysanthemum_number * chrysanthemum_price + roses_number * rose_price
    total_price = total_price_no_discount - total_price_no_discount * 0.2

print(f"{price + 2:.2f}")
