n = int(input())
time = input()

if n < 20:
    initial_fee = 0.70
    day_fee = 0.79
    night_fee = 0.9
    if time == "day":
        total_day = initial_fee + n * day_fee
        print(f"{total_day:.2f}")
    else:
        total_night = initial_fee + n * night_fee
        print(f"{total_night:.2f}")
elif n >= 100:
    fee = 0.06
    total = n * fee
    print(f"{total:.2f}")
else:
    fee = 0.09
    total = n * fee
    print(f"{total:.2f}")


