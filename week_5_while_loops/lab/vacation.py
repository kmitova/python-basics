needed_money = float(input())
available_money = float(input())
days_counter = 0
spending_days = 0

while available_money < needed_money and spending_days < 5:
    action = input()
    sum_to_use = float(input())
    days_counter = days_counter + 1
    if action == "spend":
        available_money = available_money - sum_to_use
        spending_days = spending_days + 1
        if available_money < 0:
            available_money = 0
    elif action == "save":
        available_money = available_money + sum_to_use
        spending_days = 0

if spending_days == 5:
    print(f"You can't save the money.")
    print(days_counter)

if available_money >= needed_money:
    print(f"You saved the money for {days_counter} days.")

# solving again:

# needed = float(input())
# available = float(input())
# spending_counter = 0
# days_counter = 0
#
# while available < needed and spending_counter < 5:
#     action = input()
#     money = float(input())
#     days_counter = days_counter + 1
#     if action == "spend":
#         spending_counter = spending_counter + 1
#         available = available - money
#         if available < 0:
#             available = 0
#     elif action == "save":
#         spending_counter = 0
#         available = available + money
#
#
# if spending_counter == 5:
#     print(f"you can't save. days passed = {days_counter}")
# else:
#     print(f"you saved the money for {days_counter} days")
