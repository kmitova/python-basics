groups_number = int(input())
all_members = 0
musala = 0
mon_blanc = 0
kilimandjaro = 0
k2 = 0
everest = 0
for group in range(groups_number):
    members = int(input())

    if members <= 5:  # musala
        musala = musala + members
    elif members <= 12:  # mon blanc
        mon_blanc = mon_blanc + members
    elif members <= 25:  # kilimandjaro
        kilimandjaro = kilimandjaro + members
    elif members <= 40:  # k2
        k2 = k2 + members
    elif members >= 41:  # everest
        everest = everest + members

    all_members = all_members + members

print(f"{musala / all_members * 100:.2f}%")
print(f"{mon_blanc / all_members * 100:.2f}%")
print(f"{kilimandjaro / all_members * 100:.2f}%")
print(f"{k2 / all_members * 100:.2f}%")
print(f"{everest / all_members * 100:.2f}%")
