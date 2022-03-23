processor_price_d = float(input())
card_price_d = float(input())
ram_price_d = float(input())
ram_amount = int(input())
discount = float(input())

processor_price_lv = processor_price_d * 1.57
card_price_lv = card_price_d * 1.57
ram_price_lv = ram_price_d * 1.57
ram_total = ram_price_lv * ram_amount
processor_with_discount = processor_price_lv - processor_price_lv * discount
card_with_discount = card_price_lv - card_price_lv * discount

total = ram_total + processor_with_discount + card_with_discount
print(f"Money needed - {total:.2f} leva.")
