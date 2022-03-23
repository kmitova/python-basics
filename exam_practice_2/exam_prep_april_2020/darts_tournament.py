points = int(input())
game_over = False
winning_points = 0
moves = 0
current_points = 0
while points > 0:
    sector = input()
    moves += 1
    if sector == "number section":
        current_points = int(input())
        points = points - current_points
    elif sector == "double ring":
        current_points = int(input())
        points = points - current_points * 2
    elif sector == "triple ring":
        current_points = int(input())
        points = points - current_points * 3
    elif sector == "bullseye":
        game_over = True
        winning_points = points
        break

if points == 0:
    print(f"Congratulations! You won the game in {moves} moves!")
elif game_over:
    print(f"Congratulations! You won the game with a bullseye in {moves} moves!")
else:
    print(f"Sorry, you lost. Score difference: {abs(points)}.")
