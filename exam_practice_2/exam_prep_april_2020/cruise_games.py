from math import floor
player_name = input()
played_games = int(input())
total_points = 0
volleyball_games = 0
tennis_games = 0
badminton_games = 0
volley_points = 0
tennis_points = 0
badminton_points = 0
total_volley_points = 0
total_tennis_points = 0
total_badminton_points = 0
won = False
for game in range(played_games):
    game_name = input()
    points = int(input())
    if game_name == "volleyball":
        volley_points = points
        volley_points = volley_points + volley_points * 0.07
        total_volley_points = total_volley_points + volley_points
        volleyball_games += 1
    elif game_name == "tennis":
        tennis_points = points
        tennis_points = tennis_points + tennis_points * 0.05
        total_tennis_points = total_tennis_points + tennis_points
        tennis_games += 1
    elif game_name == "badminton":
        badminton_points = points
        badminton_points = badminton_points + badminton_points * 0.02
        total_badminton_points = total_badminton_points + badminton_points
        badminton_games += 1

average_volley = (total_volley_points / volleyball_games)
average_tennis = (total_tennis_points / tennis_games)
average_badminton = (total_badminton_points / badminton_games)

if average_volley > 75 and average_tennis > 75 and average_badminton > 75:
    won = True

if won:
    print(f"Congratulations, {player_name}! You won the cruise games with {floor(total_badminton_points + total_volley_points + total_tennis_points)} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {floor(total_badminton_points + total_volley_points + total_tennis_points)}.")
