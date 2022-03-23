students_number = int(input())
students_with_two = 0
students_with_three = 0
students_with_four = 0
students_with_five = 0
grades = 0

for student in range(students_number):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        students_with_two = students_with_two + 1
    elif 3.00 <= grade <= 3.99:
        students_with_three = students_with_three + 1
    elif 4.00 <= grade <= 4.99:
        students_with_four = students_with_four + 1
    elif grade >= 5.00:
        students_with_five = students_with_five + 1
    grades = grades + grade

average_grade = grades / students_number
percent_five = students_with_five / students_number * 100
percent_four = students_with_four / students_number * 100
percent_three = students_with_three / students_number * 100
percent_two = students_with_two / students_number * 100

print(f"Top students: {percent_five:.2f}%")
print(f"Between 4.00 and 4.99: {percent_four:.2f}%")
print(f"Between 3.00 and 3.99: {percent_three:.2f}%")
print(f"Fail: {percent_two:.2f}%")
print(f"Average: {average_grade:.2f}")
