budget = float(input())
cards_number = int(input())
processors_number = int(input())
memory_number = int(input())

card_price = 250

cards_sum = cards_number * card_price
processor_sum = cards_sum * 0.35 * processors_number
memory_sum = cards_sum * 0.1 * memory_number

total_sum = cards_sum + processor_sum + memory_sum

if cards_number > processors_number:
    discount = total_sum * 0.15
    total_sum = total_sum - discount

if total_sum <= budget:
    money_left = budget - total_sum
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
