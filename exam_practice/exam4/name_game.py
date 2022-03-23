name = input()
previous_points = 0
winning_points = 0
winner = ""
first_winner = ""
while name != "Stop":
    points = 0
    for char in name:
        number_per_char = int(input())
        if number_per_char == ord(char):
            points = points + 10
        else:
            points = points + 2
    if previous_points < points:
        previous_points = points
        winner = name
        winning_points = previous_points
    elif previous_points == points:
        winner = name
    name = input()

print(f"The winner is {winner} with {winning_points} points!")

