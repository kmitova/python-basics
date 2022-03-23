n = int(input())
sum_even = 0
sum_odd = 0
for i in range(n):
    number = int(input())
    if i % 2 == 0:
        sum_even = sum_even + number
    else:
        sum_odd = sum_odd + number

if sum_odd == sum_even:
    print("Yes")
    print(f"Sum = {sum_odd}")
else:
    difference = abs(sum_odd - sum_even)
    print("No")
    print(f"Diff = {difference}")

