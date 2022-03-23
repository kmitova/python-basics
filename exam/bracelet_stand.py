pocket_money_per_day = float(input())
profit_per_day = float(input())
expenses_whole_period = float(input())
present_price = float(input())

pocket_money_saved = 5 * pocket_money_per_day
earned_money = 5 * profit_per_day
total_saved = pocket_money_saved + earned_money
total_saved_with_expenses = total_saved - expenses_whole_period

if total_saved_with_expenses >= present_price:
    print(f"Profit: {total_saved_with_expenses:.2f} BGN, the gift has been purchased.")
else:
    diff = present_price - total_saved_with_expenses
    print(f"Insufficient money: {diff:.2f} BGN.")
