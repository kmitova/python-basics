team = input()
souvenir = input()
souvenirs_amount = int(input())
price = 0
wrong_country = False
wrong_item = False
if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.2
    elif souvenir == "posters":
        price = 5.1
    elif souvenir == "stickers":
        price = 1.25
    else:
        wrong_item = True
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.2
    elif souvenir == "caps":
        price = 8.5
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.2
    else:
        wrong_item = True
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.9
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.1
    else:
        wrong_item = True
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.1
    elif souvenir == "caps":
        price = 6.5
    elif souvenir == "posters":
        price = 4.8
    elif souvenir == "stickers":
        price = 0.9
    else:
        wrong_item = True
else:
    wrong_country = True

total = price * souvenirs_amount

if wrong_item:
    print("Invalid stock!")
if wrong_country:
    print("Invalid country!")

if not wrong_item and not wrong_country:
    print(f"Pepi bought {souvenirs_amount} {souvenir} of {team} for {total:.2f} lv.")
