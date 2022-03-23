puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

order_earnings = puzzles_number * puzzle_price + \
                 dolls_number * doll_price + \
                 bears_number * bear_price + \
                 minions_number * minion_price + \
                 trucks_number * truck_price

toys_number = puzzles_number + dolls_number + \
              bears_number + minions_number + trucks_number

if toys_number >= 50:
    order_earnings = order_earnings - order_earnings * 0.25

rent = order_earnings * 0.1
income = order_earnings - rent

money_left = income - trip_price

if money_left >= 0:
    print(f"Yes! {income - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - income:.2f} lv needed.")








