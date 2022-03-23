team_name = input()
games_played = int(input())
points_total = 0
games_won = 0
games_lost = 0
games_equal = 0

for game in range(games_played):
    result = input()
    if result == "W":
        games_won += 1
        points_total += 3
    elif result == "D":
        games_equal += 1
        points_total += 1
    elif result == "L":
        games_lost += 1
        points_total = points_total

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")

else:
    print(f"{team_name} has won {points_total} points during this season.")
    print("Total stats:")
    print(f"## W: {games_won}")
    print(f"## D: {games_equal}")
    print(f"## L: {games_lost}")
    print(f"Win rate: {games_won / games_played * 100:.2f}%")
