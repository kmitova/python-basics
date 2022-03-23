number_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0

for current_number in range(number_of_numbers):
    number_to_check = int(input())
    if number_to_check % 2 == 0:
        p1 += 1
    if number_to_check % 3 == 0:
        p2 += 1
    if number_to_check % 4 == 0:
        p3 += 1

print(f"{p1 / number_of_numbers * 100:.2f}%")
print(f"{p2 / number_of_numbers * 100:.2f}%")
print(f"{p3 / number_of_numbers * 100:.2f}%")
