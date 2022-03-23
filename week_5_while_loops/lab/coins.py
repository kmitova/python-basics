sum_money = float(input())
sum_money = int(sum_money * 100)
coins_counter = 0
coins_counter = coins_counter + sum_money // 200
sum_money = sum_money % 200
coins_counter = coins_counter + sum_money // 100
sum_money = sum_money % 100
coins_counter = coins_counter + sum_money // 50
sum_money = sum_money % 50
coins_counter = coins_counter + sum_money // 20
sum_money = sum_money % 20
coins_counter = coins_counter + sum_money // 10
sum_money = sum_money % 10
coins_counter = coins_counter + sum_money // 5
sum_money = sum_money % 5
coins_counter = coins_counter + sum_money // 2
sum_money = sum_money % 2
coins_counter = coins_counter + sum_money // 1
sum_money = sum_money % 1
print(coins_counter)












