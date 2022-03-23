from math import ceil, floor

magnolia = 3.25
hyacinth = 4
rose = 3.5
cactus = 8

magnolia_num = int(input())
hyacinth_num = int(input())
rose_num = int(input())
cactus_num = int(input())
gift_price = float(input())

magnolia_sum = magnolia * magnolia_num
hyacinth_sum = hyacinth * hyacinth_num
rose_sum = rose * rose_num
cactus_sum = cactus * cactus_num
total_sum = magnolia_sum + hyacinth_sum + rose_sum + cactus_sum

tax = 0.05 * total_sum
income = total_sum - tax

if gift_price <= income:
    money_left = income - gift_price
    print(f"She is left with {floor(money_left)} leva.")

else:
    money_needed = gift_price - income
    print(f"She will have to borrow {ceil(money_needed)} leva.")

