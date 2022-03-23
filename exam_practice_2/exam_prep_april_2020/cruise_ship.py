cruise_type = input()
cabin_type = input()
nights = int(input())
price = 0

if cruise_type == "Mediterranean":
    if cabin_type == "standard cabin":
        price = 27.5
    elif cabin_type == "cabin with balcony":
        price = 30.2
    elif cabin_type == "apartment":
        price = 40.5
elif cruise_type == "Adriatic":
    if cabin_type == "standard cabin":
        price = 22.99
    elif cabin_type == "cabin with balcony":
        price = 25
    elif cabin_type == "apartment":
        price = 34.99
elif cruise_type == "Aegean":
    if cabin_type == "standard cabin":
        price = 23
    elif cabin_type == "cabin with balcony":
        price = 26.6
    elif cabin_type == "apartment":
        price = 39.8

total = price * nights * 4
if nights > 7:
    total = total - total * 0.25

print(f"Annie's holiday in the {cruise_type} sea costs {total:.2f} lv.")
