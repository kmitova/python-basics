budget = float(input())
nights = int(input())
night_price = float(input())
additional_spending_percent = int(input())

if nights > 7:
    night_price = night_price - night_price * 0.05

all_nights_price = night_price * nights
money_for_other_expenses = budget * additional_spending_percent * 0.01

money_needed = all_nights_price + money_for_other_expenses
difference = abs(money_needed - budget)
if money_needed <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
