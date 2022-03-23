from math import floor

tournaments_number = int(input())
total_points = int(input())
points_won = 0
percent_won = 0
tournaments_won = 0

for tournament in range(tournaments_number):
    level_reached = input()
    if level_reached == "W":
        points_won = points_won + 2000
        total_points = total_points + 2000
        tournaments_won = tournaments_won + 1
        percent_won = tournaments_won / tournaments_number * 100
    elif level_reached == "F":
        points_won = points_won + 1200
        total_points = total_points + 1200
    elif level_reached == "SF":
        points_won = points_won + 720
        total_points = total_points + 720

average_points = points_won / tournaments_number

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_won:.2f}%")
