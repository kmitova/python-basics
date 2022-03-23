days = int(input())
room_type = input()
rating = input()
price = 0
price_total = 0
discount = 0
room_for_one_person_price = 18
apartment_price = 25
president_apartment_price = 35
if days < 10:
    days = days -1
    if room_type == "room for one person":
        discount = 0
        price = days * room_for_one_person_price
        price_total = price
    elif room_type == "apartment":
        price = days * apartment_price
        price_total = price - price * 0.3

    elif room_type == "president apartment":
        price = days * president_apartment_price
        price_total = price - price * 0.1
elif 10 <= days <= 15:
    days = days - 1
    if room_type == "room for one person":
        discount = 0
        price_total = days * room_for_one_person_price
    elif room_type == "apartment":
        price = days * apartment_price
        price_total = price - price * 0.35

    elif room_type == "president apartment":
        price = days * president_apartment_price
        price_total = price - price * 0.15
elif days > 15:
    days = days - 1
    if room_type == "room for one person":
        discount = 0
        price = days * room_for_one_person_price
        price_total = price
    elif room_type == "apartment":
        price = days * apartment_price
        price_total = price - price * 0.5
    elif room_type == "president apartment":
        price = days * president_apartment_price
        price_total = price - price * 0.2

if rating == "positive":
    price_total = price_total + price_total * 0.25
elif rating == "negative":
    price_total = price_total - price_total * 0.1


print(f"{price_total:.2f}")


