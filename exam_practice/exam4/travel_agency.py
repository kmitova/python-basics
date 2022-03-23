name = input()
package_type = input()
VIP = input()
days_to_stay = int(input())
price_per_day = 0
total = 0
invalid_input = False

if name == "Bansko" or name == "Borovets":
    if package_type == "withEquipment":
        price_per_day = 100
        if VIP == "yes":
            price_per_day = price_per_day - price_per_day * 0.1
    elif package_type == "noEquipment":
        price_per_day = 80
        if VIP == "yes":
            price_per_day = price_per_day - price_per_day * 0.05
    else:
        invalid_input = True
elif name == "Varna" or name == "Burgas":
    if package_type == "withBreakfast":
        price_per_day = 130
        if VIP == "yes":
            price_per_day = price_per_day - price_per_day * 0.12
    elif package_type == "noBreakfast":
        price_per_day = 100
        if VIP == "yes":
            price_per_day = price_per_day - price_per_day * 0.07
    else:
        invalid_input = True
else:
    invalid_input = True

if invalid_input:
    print("Invalid input!")
else:
    if days_to_stay > 7:
        days_to_stay = days_to_stay - 1
        total = price_per_day * days_to_stay
        print(f"The price is {total:.2f}lv! Have a nice time!")
    elif 1 <= days_to_stay <= 7:
        total = price_per_day * days_to_stay
        print(f"The price is {total:.2f}lv! Have a nice time!")
    else:
        print("Days must be positive number!")
