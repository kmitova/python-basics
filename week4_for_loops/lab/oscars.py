actor_name = input()
total_points = float(input())
jury_number = int(input())

for current_grade in range(jury_number):
    jury_member_name = input()
    current_points = float(input())
    current_final_points = len(jury_member_name) * current_points / 2
    total_points = total_points + current_final_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")

