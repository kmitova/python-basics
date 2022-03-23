number = int(input())

a = number % 10
b = number // 10 % 10
c = number // 100
result = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            result = i * j * k
            print(f"{i} * {j} * {k} = {result};")