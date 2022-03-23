from math import floor

width = float(input())
length = float(input())
height = float(input())
astronauts_height = float(input())

volume_total = width * height * length
volume_room = (astronauts_height + 0.4) * 2 * 2
available = floor(volume_total / volume_room)

if 3 <= available <= 10:
    print(f"The spacecraft holds {available} astronauts.")
elif available < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
