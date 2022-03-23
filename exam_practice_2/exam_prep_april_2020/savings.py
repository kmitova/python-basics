monthly_income = float(input())
months = int(input())
sum_for_expenses = float(input())

sum_for_unpredicted = 0.3 * monthly_income
sum_to_save = monthly_income - (sum_for_unpredicted + sum_for_expenses)
total_saved = months * sum_to_save
percent = sum_to_save / monthly_income * 100

print(f"She can save {percent:.2f}%")
print(f"{total_saved:.2f}")
