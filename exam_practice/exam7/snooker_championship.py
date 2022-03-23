stage = input()
ticket_type = input()
number_of_tickets = int(input())
photo = input()
price = 0
photos_free = False
if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.5
    elif ticket_type == "Premium":
        price = 105.2
    else:
        price = 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    else:
        price = 300.4
else:
    if ticket_type == "Standard":
        price = 110.1
    elif ticket_type == "Premium":
        price = 160.66
    else:
        price = 400

photo_price = 0
total = number_of_tickets * price
if total > 4000:
    total = total - total * 0.25
    photos_free = True
elif 2500 < total <= 4000:
    total = total - total * 0.1

if photo == "Y" and photos_free:
    total = total
elif not photos_free and photo == "N":
    total = total
elif not photos_free:
    photo_price = 40 * number_of_tickets
    total = total + photo_price

print(f"{total:.2f}")
