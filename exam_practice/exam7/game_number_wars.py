name_1 = input()
name_2 = input()
command_1 = input()
command_2 = input()
points_1 = 0
points_2 = 0
winner = ""
while command_1 != "End of game" or command_2 != "End of game":
    card_1 = int(command_1)
    card_2 = int(command_2)
    if card_1 > card_2:
        points_1 = points_1 + card_1 - card_2
    elif card_1 < card_2:
        points_2 = points_2 + card_2 - card_1
    elif card_1 == card_2:
        print("Number wars!")
        card_1 = int(input())
        card_2 = int(input())
        if card_1 > card_2:
            winner = name_1
            print(f"{name_1} is winner with {points_1} points")
            break
        else:
            winner = name_2
            print(f"{name_2} is winner with {points_2} points")
            break
    command_1 = input()
    if command_1 == "End of game":
        break
    command_2 = input()
    if command_2 == "End of game":
        break

if command_1 == "End of game" or command_2 == "End of game":
    print(f"{name_1} has {points_1} points")
    print(f"{name_2} has {points_2} points")
