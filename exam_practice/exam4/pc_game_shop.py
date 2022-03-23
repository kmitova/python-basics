games_sold = int(input())
hearthstone_sold = 0
fortnite_sold = 0
overwatch_sold = 0
others_sold = 0
for game in range(games_sold):
    name = input()
    if name == "Hearthstone":
        hearthstone_sold += 1
    elif name == "Fornite":
        fortnite_sold += 1
    elif name == "Overwatch":
        overwatch_sold += 1
    else:
        others_sold += 1

hearthstone_percent = hearthstone_sold / games_sold * 100
fortnite_percent = fortnite_sold / games_sold * 100
overwatch_percent = overwatch_sold / games_sold * 100
others_percent = others_sold / games_sold * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fortnite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
