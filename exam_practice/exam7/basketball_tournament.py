name_of_tournament = input()
wins = 0
losses = 0
total_games = 0
while name_of_tournament != "End of tournaments":
    games_per_tournament = int(input())
    total_games = total_games + games_per_tournament
    games_played = 0
    difference_1 = 0
    difference_2 = 0
    for game in range(games_per_tournament):
        points_1 = int(input())
        points_2 = int(input())
        games_played += 1
        if points_1 > points_2:
            difference_1 = points_1 - points_2
            wins += 1
            print(f"Game {games_played} of tournament {name_of_tournament}: win with {difference_1} points.")
        else:
            difference_2 = points_2 - points_1
            losses += 1
            print(f"Game {games_played} of tournament {name_of_tournament}: lost with {difference_2} points.")
    name_of_tournament = input()


percent_won = wins / total_games * 100
percent_lost = losses / total_games * 100
print(f"{percent_won:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
