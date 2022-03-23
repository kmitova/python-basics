from math import ceil

speed = float(input())
gasoline_per_100_km = float(input())

distance = 384400 * 2
time = ceil(distance / speed)
total_time = time + 3
gasoline = (gasoline_per_100_km * distance) / 100

print(total_time)
print(int(gasoline))
