visitors = int(input())
training_back = 0
training_chest = 0
training_legs = 0
training_abs = 0
bought_shake = 0
bought_bar = 0
come_to_train = 0
come_to_buy = 0

for visitor in range(visitors):
    activity = input()
    if activity == "Back":
        training_back += 1
        come_to_train += 1
    elif activity == "Chest":
        training_chest += 1
        come_to_train += 1
    elif activity == "Abs":
        training_abs += 1
        come_to_train += 1
    elif activity == "Legs":
        training_legs += 1
        come_to_train += 1
    elif activity == "Protein shake":
        bought_shake += 1
        come_to_buy += 1
    elif activity == "Protein bar":
        bought_bar += 1
        come_to_buy += 1

percent_come_to_train = come_to_train / visitors * 100
percent_come_to_buy = come_to_buy / visitors * 100

print(f"{training_back} - back")
print(f"{training_chest} - chest")
print(f"{training_legs} - legs")
print(f"{training_abs} - abs")
print(f"{bought_shake} - protein shake")
print(f"{bought_bar} - protein bar")
print(f"{percent_come_to_train:.2f}% - work out")
print(f"{percent_come_to_buy:.2f}% - protein")

