peak_reached = False
days_counter = 1
total_meters = 5364
command = input()
while command != "END":
    answer = command
    meters = int(input())
    if answer == "Yes":
        days_counter += 1
    if days_counter > 5:
        break
    total_meters = total_meters + meters
    if total_meters > 8848:
        peak_reached = True
        break
    command = input()

if peak_reached:
    print(f"Goal reached for {days_counter} days!")
else:
    print("Failed!")
    print(f"{total_meters}")
