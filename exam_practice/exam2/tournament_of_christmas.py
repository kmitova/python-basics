days = int(input())
days_won = 0
days_lost = 0
total_money_won = 0
finish = False

for day in range(1, days + 1):
    money_won_for_the_day = 0
    games_won = 0
    games_lost = 0
    while True:
        command = input()
        if command == "Finish":
            finish = True
            break
        sport = command
        result = input()
        if result == "win":
            money_won_for_the_day = money_won_for_the_day + 20
            games_won = games_won + 1
        elif result == "lose":
            games_lost = games_lost + 1

    if games_won > games_lost:
        money_won_for_the_day = money_won_for_the_day + money_won_for_the_day * 0.1
        total_money_won = total_money_won + money_won_for_the_day
        days_won = days_won + 1
    else:
        days_lost = days_lost + 1
        total_money_won = total_money_won + money_won_for_the_day

if days_won > days_lost:
    total_money_won = total_money_won + total_money_won * 0.2
    print(f"You won the tournament! Total raised money: {total_money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_won:.2f}")

