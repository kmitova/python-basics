from math import ceil

name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
rest_time = break_duration * 1/4
time_remaining = break_duration - (lunch_time + rest_time)

if time_remaining >= episode_duration:
    print(f"You have enough time to watch {name} "
          f"and left with {ceil(time_remaining - episode_duration)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {name},"
          f" you need {ceil(episode_duration - time_remaining)} more minutes.")
