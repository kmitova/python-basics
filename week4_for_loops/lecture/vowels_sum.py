text = input()

total_sum = 0

for char in text:
    if char == "a":
        number = 1
        total_sum = total_sum + number
    elif char == "e":
        number = 2
        total_sum = total_sum + number
    elif char == "i":
        number = 3
        total_sum = total_sum + number
    elif char == "o":
        number = 4
        total_sum = total_sum + number
    elif char == "u":
        number = 5
        total_sum = total_sum + number

print(total_sum)
