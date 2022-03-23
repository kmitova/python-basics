student_name = input()
fails = 0
year = 1
is_expelled = False
grades = 0
while year <= 12:
    current_grade = float(input())
    if current_grade < 4.00:
        fails = fails + 1
        if fails == 2:
            is_expelled = True
            break
        continue
    grades = grades + current_grade
    year = year + 1

if is_expelled:
    print(f"{student_name} has been excluded at {year} grade")
else:
    average_grade = grades / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
