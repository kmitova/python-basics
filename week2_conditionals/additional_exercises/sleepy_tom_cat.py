max_play = 30000
work_day_play = 63
rest_day_play = 127
rest_days = int(input())

rest_days_play_total = rest_day_play * rest_days
work_days = 365 - rest_days
work_days_play_total = work_day_play * work_days
play_time_total = rest_days_play_total + work_days_play_total

if play_time_total > max_play:
    time_over = play_time_total - max_play
    hours = time_over // 60
    minutes = time_over % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    time_left = max_play - play_time_total
    hours = time_left // 60
    minutes = time_left % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
