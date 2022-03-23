sea_trips_available = int(input())
mountain_trips_available = int(input())
profit = 0
all_sold = False

while True:
    command = input()
    if command == "Stop":
        break
    trip_type = command

    if trip_type == "sea":
        if sea_trips_available <= 0:
            continue
        sea_trips_available = sea_trips_available - 1
        profit = profit + 680
    elif trip_type == "mountain":
        if mountain_trips_available <= 0:
            continue
        mountain_trips_available = mountain_trips_available - 1
        profit = profit + 499
    if sea_trips_available <= 0 and mountain_trips_available <= 0:
        all_sold = True
        break
    # command = input()

if all_sold:
    print("Good job! Everything is sold.")

print(f"Profit: {profit} leva.")
