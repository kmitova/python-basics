dancers_number = int(input())
points = float(input())
season = input()
place = input()
percent = 0

if season == "summer":
    if place == "Bulgaria":
        percent = 5
    else:
        percent = 10
elif season == "winter":
    if place == "Bulgaria":
        percent = 8
    else:
        percent = 15

money_won = dancers_number * points

if place == "Abroad":
    money_won = money_won + money_won * 0.5

money_won = money_won - money_won * percent / 100
money_for_charity = money_won * 0.75
money_left = money_won - money_for_charity
ind_money = money_left / dancers_number


print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {ind_money:.2f}")
