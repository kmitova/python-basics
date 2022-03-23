season = input()
km_per_month = int(input())
income_per_km = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        income_per_km = 0.75
    elif season == "Summer":
        income_per_km = 0.9
    elif season == "Winter":
        income_per_km = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        income_per_km = 0.95
    elif season == "Summer":
        income_per_km = 1.1
    elif season == "Winter":
        income_per_km = 1.25
elif 10000 < km_per_month <= 20000:
    income_per_km = 1.45

income = km_per_month * income_per_km * 4
earnings = income - income * 0.1

print(f"{earnings:.2f}")
