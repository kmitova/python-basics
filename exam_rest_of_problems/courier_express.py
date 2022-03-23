weight = float(input())
service = input()
distance = int(input())
price_per_km = 0
add = 0
if service == "standard":
    if weight < 1:
        price_per_km = 0.03
    elif weight < 10:
        price_per_km = 0.05
    elif 10 <= weight < 40:
        price_per_km = 0.10
    elif weight < 90:
        price_per_km = 0.15
    elif weight <= 150:
        price_per_km = 0.20
elif service == "express":
    if weight < 1:
        add = 0.03 * 0.8
        price_per_km = 0.03
    elif weight < 10:
        add = 0.05 * 0.4
        price_per_km = 0.05
    elif 10 <= weight < 40:
        add = 0.10 * 0.05
        price_per_km = 0.10
    elif weight < 90:
        add = 0.15 * 0.02
        price_per_km = 0.15
    elif weight <= 150:
        add = 0.20 * 0.01
        price_per_km = 0.20

add_kgs = add * weight
add_distance = add_kgs * distance
total = price_per_km * distance
price = total + add_distance
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")
