n = int(input())
sum_one = 0
sum_two = 0
for i in range(n):
    number_one = int(input())
    sum_one = sum_one + number_one
for i in range(n):
    number_two = int(input())
    sum_two = sum_two + number_two

if sum_one == sum_two:
    print(f"Yes, sum = {sum_one}")
else:
    difference = abs(sum_one - sum_two)
    print(f"No, diff = {difference}")


