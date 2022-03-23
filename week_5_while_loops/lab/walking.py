goal = 10000
total_steps = 0
while total_steps < goal:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        total_steps = total_steps + steps_to_home
        break
    current_steps = int(command)
    total_steps = total_steps + current_steps
difference = abs(total_steps - goal)
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{abs(difference)} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")


# solving again

# goal = 10000
# total_steps = 0
#
# while total_steps < goal:
#     command = input()
#     if command == "Going home":
#         steps_to_home = int(input())
#         total_steps = total_steps + steps_to_home
#         break
#     steps = int(command)
#     total_steps = total_steps + steps
#
# difference = abs(total_steps - goal)
#
# if total_steps >= goal:
#     print("Goal reached! Good job!")
#     print(f"{difference} steps over the goal!")
# else:
#     print(f"{difference} more steps to reach goal.")
























