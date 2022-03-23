days = int(input())
hours_per_day = int(input())
total_to_pay_per_day = 0
total_pay_all_days = 0
pay_per_hour = 0
day_index = 0

for day in range(1, days + 1):
    day_index = day_index + 1

    total_to_pay_per_day = 0

    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_to_pay_per_day = total_to_pay_per_day + 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_to_pay_per_day = total_to_pay_per_day + 1.25
        else:
            total_to_pay_per_day = total_to_pay_per_day + 1
    print(f"Day: {day_index} - {total_to_pay_per_day:.2f} leva")
    total_pay_all_days = total_pay_all_days + total_to_pay_per_day

print(f"Total: {total_pay_all_days:.2f} leva")
