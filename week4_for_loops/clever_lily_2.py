age = int(input())
goal = float(input())
price_per_toy = float(input())
toys = 0
money = 0
money_per_year = 10
received_money_times = 0

for year in range(1, age+1):
    if year % 2 == 0:
        money += money_per_year
        money_per_year += 10
        received_money_times += 1
    else:
        toys += 1

toys_money = toys * price_per_toy
money = money - received_money_times
total = toys_money + money

diff = abs(goal - total)
if total >= goal:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
