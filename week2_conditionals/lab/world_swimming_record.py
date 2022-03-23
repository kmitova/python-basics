current_record = float(input())
meters = float(input())
time_per_m = float(input())

time = meters * time_per_m
time_delay = (meters // 15) * 12.5
total_time = time + time_delay

if total_time < current_record:
    print(f" Yes, he succeeded! The new world record is"
          f" {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(current_record - total_time):.2f} "
          f"seconds slower.")
