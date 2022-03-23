message = 0.6
rose = 7.2
keyholder = 3.6
caricature = 18.2
surprise = 22

money_needed = float(input())
messages_number = int(input())
roses_number = int(input())
keyholders_number = int(input())
caricatures_number = int(input())
surprises_number = int(input())

total = messages_number * message + roses_number * rose + keyholders_number * keyholder + caricatures_number * \
        caricature + surprises_number * surprise
orders = messages_number + roses_number + keyholders_number + caricatures_number + surprises_number
if orders >= 25:
    total = total * 0.65

total = total * 0.9
diff = abs(money_needed - total)

if total >= money_needed:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
