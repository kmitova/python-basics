moves_of_game = int(input())
result = 0
number_9 = 0
number_19 = 0
number_29 = 0
number_39 = 0
number_50 = 0
invalid_numbers = 0

for move in range(moves_of_game):
    number = int(input())
    if 0 <= number <= 9:
        result = result + number * 0.2
        number_9 = number_9 + 1
    elif 10 <= number <= 19:
        result = result + number * 0.3
        number_19 = number_19 + 1
    elif 20 <= number <= 29:
        result = result + number * 0.4
        number_29 = number_29 + 1
    elif 30 <= number <= 39:
        result = result + 50
        number_39 = number_39 + 1
    elif 40 <= number <= 50:
        result = result + 100
        number_50 = number_50 + 1
    if number > 50 or number < 0:
        result = result / 2
        invalid_numbers = invalid_numbers + 1

percent_9 = number_9 / moves_of_game * 100
percent_19 = number_19 / moves_of_game * 100
percent_29 = number_29 / moves_of_game * 100
percent_39 = number_39 / moves_of_game * 100
percent_50 = number_50 / moves_of_game * 100
invalid_percent = invalid_numbers / moves_of_game * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_9:.2f}%")
print(f"From 10 to 19: {percent_19:.2f}%")
print(f"From 20 to 29: {percent_29:.2f}%")
print(f"From 30 to 39: {percent_39:.2f}%")
print(f"From 40 to 50: {percent_50:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")
