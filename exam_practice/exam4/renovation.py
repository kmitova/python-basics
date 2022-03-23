from math import ceil

height = int(input())
width = int(input())
percent_not_to_paint = int(input())
total_area = 4 * height * width
area_to_paint = ceil(total_area - total_area * percent_not_to_paint * 0.01)
area_to_paint_2 = area_to_paint
total_paint = 0
command = input()
while command != "Tired!":
    liters_paint = int(command)
    total_paint = total_paint + liters_paint
    area_to_paint = area_to_paint - liters_paint
    if area_to_paint_2 < total_paint:
        print(f"All walls are painted and you have {total_paint - area_to_paint_2} l paint left!")
        break
    if area_to_paint_2 == total_paint:
        print("All walls are painted! Great job, Pesho!")
        break
    command = input()

if command == "Tired!":
    print(f"{area_to_paint} quadratic m left.")
