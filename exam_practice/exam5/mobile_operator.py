duration = input()
contract_type = input()
data_or_not = input()
months = int(input())
price = 0

if contract_type == "Small":
    if duration == "one":
        price = 9.98
    elif duration == "two":
        price = 8.58
elif contract_type == "Middle":
    if duration == "one":
        price = 18.99
    elif duration == "two":
        price = 17.09
elif contract_type == "Large":
    if duration == "one":
        price = 25.98
    elif duration == "two":
        price = 23.59
elif contract_type == "ExtraLarge":
    if duration == "one":
        price = 35.99
    elif duration == "two":
        price = 31.79

if data_or_not == "yes":
    if price <= 10:
        price = price + 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if duration == "two":
    price = price - price * 0.0375

total_price = price * months

print(f"{total_price:.2f} lv.")
