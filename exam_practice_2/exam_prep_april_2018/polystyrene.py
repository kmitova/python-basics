from math import ceil

budget = float(input())
total_area = float(input())
windows= int(input())
m2_in_pack = float(input())
price_per_pack = float(input())

area = total_area - windows * 2.4
area = area + area * 0.1
packs_needed = ceil(area/ m2_in_pack)
price = packs_needed * price_per_pack

if price <= budget:
    print(f"Spent: {price:.2f}")
    print(f"Left: {budget - price:.2f}")
else:
    print(f"Need more: {price - budget:.2f}")
