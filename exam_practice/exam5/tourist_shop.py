budget = float(input())
command = input()
remaining_money = 0
product_counter = 0
total_spent = 0
difference = 0
not_enough_money = False
while command != "Stop":
    product = command
    product_price = float(input())
    product_counter = product_counter + 1
    if product_counter % 3 == 0:
        product_price = product_price / 2
    if product_price > budget:
        not_enough_money = True
        difference = product_price - budget
        break
    budget = budget - product_price
    total_spent = total_spent + product_price
    command = input()

if not_enough_money:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")

else:
    print(f"You bought {product_counter} products for {total_spent:.2f} leva.")
