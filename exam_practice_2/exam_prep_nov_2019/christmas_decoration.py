budget = int(input())
no_money_left = False
command = input()

while command != "Stop":
    product = command
    price = 0
    for char in product:
        price = price + ord(char)
    if budget < price:
        no_money_left = True
        break
    else:
        budget = budget - price
        print("Item successfully purchased!")

    command = input()

if no_money_left:
    print("Not enough money!")

elif command == "Stop":
    print(f"Money left: {budget}")
