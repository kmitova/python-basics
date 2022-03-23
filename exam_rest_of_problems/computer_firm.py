number_of_models = int(input())
made_sales = 0
sale = 0
all_ratings = 0

for model in range(number_of_models):
    number = int(input())
    rating = number % 10
    profit = number // 10
    if rating == 3:
        sale = profit * 0.5
    elif rating == 2:
        sale = 0
    elif rating == 4:
        sale = profit * 0.7
    elif rating == 5:
        sale = profit * 0.85
    elif rating == 6:
        sale = profit
    made_sales = made_sales + sale
    all_ratings = all_ratings + rating
average_rating = all_ratings / number_of_models

print(f"{made_sales:.2f}")
print(f"{average_rating:.2f}")
