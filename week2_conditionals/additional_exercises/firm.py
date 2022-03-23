from math import floor, ceil

hours_needed = int(input())
days = int(input())
staff_number_overtime = int(input())
days_available = days - days * 0.1
work_day = 8
overtime = 2
work_hours_per_person_max = work_day + overtime

work_time_hours_for_project = days_available * work_day
overtime_total = staff_number_overtime * (2 * days)

total_time = work_time_hours_for_project + overtime_total

if total_time < hours_needed:
    time_left = hours_needed - total_time
    print(f"Not enough time!{ceil(time_left)} hours needed.")
else:
    more_time_needed = total_time - hours_needed
    print(f"Yes!{floor(more_time_needed)} hours left.")