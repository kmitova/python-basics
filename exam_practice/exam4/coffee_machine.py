drink = input()
sugar = input()
amount = int(input())
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7

total_price = price * amount
if sugar == "Without":
    total_price = total_price - total_price * 0.35
if drink == "Espresso" and amount >= 5:
    total_price = total_price - total_price * 0.25
if total_price > 15:
    total_price = total_price - total_price * 0.2

print(f"You bought {amount} cups of {drink} for {total_price:.2f} lv.")