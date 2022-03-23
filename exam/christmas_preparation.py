paper_rolls = int(input())
textile_rolls = int(input())
glue_liters = float(input())
discount = int(input())

paper_price = paper_rolls * 5.8
textile_price = 7.2 * textile_rolls
glue_price = 1.2 * glue_liters
total = paper_price + textile_price + glue_price
total_with_discount = total - total * discount / 100
print(f"{total_with_discount:.3f}")
