n = int(input())
counter = 0
reached = False
for a in range(1, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, -1):
                if n % 10 == 5 and a+b+c+d == a*b*c*d:
                    counter += 1
                    print(f"{a}{b}{c}{d}")
                    reached = True
                    break
                elif a*b*c*d // a+b+c+d == 3 and n % 3 == 0:
                    counter += 1
                    print(f"{d}{c}{b}{a}")
                    reached = True
                    break
            if reached:
                break
        if reached:
            break
    if reached:
        break

if counter == 0:
    print("Nothing found")
