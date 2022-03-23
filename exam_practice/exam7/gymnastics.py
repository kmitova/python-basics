country = input()
tool = input()
difficulty_grade = 0
execution_grade = 0

if country == "Russia":
    if tool == "ribbon":
        difficulty_grade = 9.100
        execution_grade = 9.400
    elif tool == "hoop":
        difficulty_grade = 9.300
        execution_grade = 9.800
    elif tool == "rope":
        difficulty_grade = 9.600
        execution_grade = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty_grade = 9.600
        execution_grade = 9.400
    elif tool == "hoop":
        difficulty_grade = 9.550
        execution_grade = 9.750
    elif tool == "rope":
        difficulty_grade = 9.500
        execution_grade = 9.400
elif country == "Italy":
    if tool == "ribbon":
        difficulty_grade = 9.200
        execution_grade = 9.500
    elif tool == "hoop":
        difficulty_grade = 9.450
        execution_grade = 9.350
    elif tool == "rope":
        difficulty_grade = 9.700
        execution_grade = 9.150

final_grade = difficulty_grade + execution_grade
max_grade = 20

needed = max_grade - final_grade
percent_needed = needed / max_grade * 100

print(f'The team of {country} get {final_grade:.3f} on {tool}.')
print(f"{percent_needed:.2f}%")

