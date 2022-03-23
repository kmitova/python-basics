bitcoins = int(input())
chinese = float(input())
commission = float(input())

bitcoins_to_lv = bitcoins * 1168
chinese_to_dollars = 0.15 * chinese
dollars_to_lv = chinese_to_dollars * 1.76
lv_total = bitcoins_to_lv + dollars_to_lv
euro = lv_total / 1.95
total_euro = euro - euro * commission * 0.01
print(f"{total_euro:.2f}")
