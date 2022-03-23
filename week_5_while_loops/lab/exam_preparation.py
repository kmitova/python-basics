fails_threshold = int(input())
solved_problems = 0
fails = 0
grades = 0
last_problem = ""
has_failed = True
while fails < fails_threshold:
    name = input()
    if name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        fails = fails + 1

    solved_problems += 1
    grades = grades + grade
    last_problem = name

if has_failed:
    print(f"You need a break, {fails} poor grades.")
else:
    average = grades / solved_problems
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {solved_problems}")
    print(f"Last problem: {last_problem}")

# solving again:

# fails_threshold = int(input())
# fails = 0
# grade = 0
# grades = 0
# last_problem = ""
# number_of_problems = 0
#
# while fails < fails_threshold:
#     problem_name = input()
#     if problem_name == "Enough":
#         break
#     grade = int(input())
#     if grade <= 4:
#         fails = fails + 1
#     grades = grades + grade
#     number_of_problems = number_of_problems + 1
#     last_problem = problem_name
#
# average = grades / number_of_problems
#
# if fails >= fails_threshold:
#     print(fails)
# else:
#     print(average)
#     print(number_of_problems)
#     print(last_problem)































