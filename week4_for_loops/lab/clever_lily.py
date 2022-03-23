age = int(input())
money_needed = float(input())
toy_price = int(input())

money_saved = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money_saved = money_saved + (birthday * 10 / 2) - 1
    else:
        money_saved = money_saved + toy_price

if money_saved >= money_needed:
    print(f"Yes! {money_saved - money_needed:.2f}")
else:
    print(f"No! {money_needed - money_saved:.2f}")
