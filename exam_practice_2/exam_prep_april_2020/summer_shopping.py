budget = int(input())
towel_price = float(input())
discount = int(input())

umbrella_price = 2/3 * towel_price
sandals = 0.75 * umbrella_price
bag = (towel_price + sandals) / 3
total = towel_price + umbrella_price + sandals + bag
total_with_discount = total - total * discount / 100

if budget >= total_with_discount:
    print(f"Annie's sum is {total_with_discount:.2f} lv. She has {budget - total_with_discount:.2f} lv. left.")
else:
    print(f"Annie's sum is {total_with_discount:.2f} lv. She needs {total_with_discount - budget:.2f} lv. more.")
