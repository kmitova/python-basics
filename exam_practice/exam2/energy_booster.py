fruit = input()
size = input()
number_of_sets = int(input())
price_for_one = 0
price = 0

if fruit == "Watermelon":
    if size == "small":
        price_for_one = 56
        price = price_for_one * 2
    elif size == "big":
        price_for_one = 28.7
        price = price_for_one * 5
elif fruit == "Mango":
    if size == "small":
        price_for_one = 36.66
        price = price_for_one * 2
    elif size == "big":
        price_for_one = 19.6
        price = price_for_one * 5
elif fruit == "Pineapple":
    if size == "small":
        price_for_one = 42.1
        price = price_for_one * 2
    elif size == "big":
        price_for_one = 24.8
        price = price_for_one * 5
elif fruit == "Raspberry":
    if size == "small":
        price_for_one = 20
        price = price_for_one * 2
    elif size == "big":
        price_for_one = 15.2
        price = price_for_one * 5

total_price = number_of_sets * price

if 400 <= total_price <= 1000:
    total_price = total_price - total_price * 0.15
elif total_price > 1000:
    total_price = total_price - total_price * 0.5

print(f"{total_price:.2f} lv.")
