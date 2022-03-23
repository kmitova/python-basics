six_changes = False
changes_counter = 0
k = int(input())
l = int(input())
m = int(input())
n = int(input())

for a in range(k, 8 + 1):
    for b in range(9, l - 1, -1):
        for c in range(m, 8 + 1):
            for d in range(9, n - 1, -1):
                if a % 2 == 0 and c % 2 == 0:
                    if b % 2 != 0 and d % 2 != 0:
                        if f"{a}{b}" != f"{c}{d}":
                            changes_counter += 1
                            print(f"{a}{b} - {c}{d}")
                        else:
                            print("Cannot change the same player.")
                    if changes_counter >= 6:
                        six_changes = True
                        break
            if six_changes:
                break
        if six_changes:
            break
    if six_changes:
        break
