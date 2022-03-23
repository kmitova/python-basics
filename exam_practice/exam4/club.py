income_wanted = float(input())
income_earned = 0
cocktail_price = 0
order_price = 0
party_command = False
while income_earned < income_wanted:
    cocktail_name = input()
    if cocktail_name == "Party!":
        party_command = True
        break
    cocktails_in_an_order = int(input())
    cocktail_price = len(cocktail_name)
    order_price = cocktail_price * cocktails_in_an_order
    if order_price % 2 != 0:
        order_price = order_price - order_price * 0.25
    income_earned = income_earned + order_price

if party_command:
    needed = income_wanted - income_earned
    print(f"We need {needed:.2f} leva more.")
else:
    print("Target acquired.")

print(f"Club income - {income_earned:.2f} leva.")
