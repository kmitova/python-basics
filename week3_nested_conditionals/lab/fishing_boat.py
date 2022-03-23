budget = int(input())
season = input()
fishermen = int(input())
rent = 0
price = 0


if season == "Spring":
    rent = 3000
    if fishermen <= 6:
        price = rent - rent * 0.1
    elif 6 < fishermen <= 11:
        price = rent - rent * 0.15
    elif fishermen >= 12:
        price = rent - rent * 0.25
    if fishermen % 2 == 0:
        price = price - price * 0.05

elif season == "Summer":
    rent = 4200
    if fishermen <= 6:
        price = rent - rent * 0.1
    elif 6 < fishermen <= 11:
        price = rent - rent * 0.15
    elif fishermen >= 12:
        price = rent - rent * 0.25
    if fishermen % 2 == 0:
        price = price - price * 0.05
elif season == "Autumn":
    rent = 4200
    if fishermen <= 6:
        price = rent - rent * 0.1
    elif 6 < fishermen <= 11:
        price = rent - rent * 0.15
    elif fishermen >= 12:
        price = rent - rent * 0.25

elif season == "Winter":
    rent = 2600
    if fishermen <= 6:
        price = rent - rent * 0.1
    elif 6 < fishermen <= 11:
        price = rent - rent * 0.15
    elif fishermen >= 12:
        price = rent - rent * 0.25
    if fishermen % 2 == 0:
        price = price - price * 0.05

if budget - price >= 0:
    left_money = budget - price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")



