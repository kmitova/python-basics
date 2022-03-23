month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
studio_price_total = 0
apartment_price_total = 0

if month == "May" or month == "October":
    apartment_price = 65 * nights
    studio_price = 50 * nights

    if 7 < nights <= 14:
        studio_price -= studio_price * 0.05
    if nights > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10
elif month == "June" or month == "September":
    apartment_price = 68.70 * nights
    studio_price = 75.20 * nights
    if nights > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10
elif month == "August" or month == "July":
    apartment_price = 77 * nights
    studio_price = 76 * nights

    if nights > 14:
        apartment_price -= apartment_price * 0.10

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
