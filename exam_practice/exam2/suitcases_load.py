capacity = float(input())
bag_volume = input()
total_volume = 0
bags_loaded = 0

while bag_volume != "End":
    current_volume = float(bag_volume)
    bags_loaded += 1
    if bags_loaded % 3 == 0:
        total_volume += current_volume + current_volume * 0.1
    else:
        total_volume += current_volume
    if capacity < total_volume:
        bags_loaded = bags_loaded - 1
        break
    bag_volume = input()

if total_volume > capacity:
    print("No more space!")
    print(f"Statistic: {bags_loaded} suitcases loaded.")
else:
    print(f"Congratulations! All suitcases are loaded!")
    print(f"Statistic: {bags_loaded} suitcases loaded.")
