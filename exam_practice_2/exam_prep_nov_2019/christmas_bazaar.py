from math import floor

goal_sum = float(input())
fantasy_books = int(input())
horror_books = int(input())
romance_books = int(input())

romance_total = romance_books * 4.3
horror_total = horror_books * 9.8
fantasy_total = fantasy_books * 14.9

total = romance_total + horror_total + fantasy_total
dds = total * 0.2
total_after_dds = total - dds

if total_after_dds > goal_sum:
    remaining = total_after_dds - goal_sum
    bonus = remaining * 0.1
    remaining_after_bonus = remaining - bonus
    total = goal_sum + remaining_after_bonus
    print(f"{total:.2f} leva donated.")
    print(f"Sellers will receive {floor(bonus)} leva.")
else:
    print(f"{goal_sum - total_after_dds:.2f} money needed.")

