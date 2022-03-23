control_minutes = int(input())
control_seconds = int(input())
length_m = float(input())
seconds_for_100m = int(input())

control_in_s = control_minutes * 60 + control_seconds  #132
delay = length_m / 120  # 10
delay_time = delay * 2.5  # 25
time = length_m / 100 * seconds_for_100m - delay_time

if time <= control_in_s:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    needed = time - control_in_s
    print(f"No, Marin failed! He was {needed:.3f} second slower.")
