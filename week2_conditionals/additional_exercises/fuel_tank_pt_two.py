gasoline_liter_price = 2.22
diesel_liter_price = 2.33
gas_liter_price = 0.93

fuel_type = input()
fuel_quantity = float(input())
discount_card = input()

if fuel_type == "Gasoline":
    if discount_card == "Yes":
        gasoline_liter_price_discounted = gasoline_liter_price - 0.18
        price = gasoline_liter_price_discounted * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    else:
        price = gasoline_liter_price * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
elif fuel_type == "Diesel":
    if discount_card == "Yes":
        diesel_liter_price_discounted = diesel_liter_price - 0.12
        price = diesel_liter_price_discounted * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    else:
        price = diesel_liter_price * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
elif fuel_type == "Gas":
    if discount_card == "Yes":
        gas_liter_price_discounted = gas_liter_price - 0.08
        price = gas_liter_price_discounted * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
    else:
        price = gas_liter_price * fuel_quantity
        if 20 <= fuel_quantity <= 25:
            price_with_discount = price - price * 0.08
            print(f"{price_with_discount:.2f} lv.")
        elif fuel_quantity > 25:
            price_with_discount = price - price * 0.1
            print(f"{price_with_discount:.2f} lv.")
        else:
            print(f"{price:.2f} lv.")
