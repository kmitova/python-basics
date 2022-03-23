inheritance = float(input())
year_to_live_to = int(input())
age = 18

for year in range(1800, year_to_live_to + 1):
    if year % 2 == 0:
        inheritance = inheritance - 12000
    else:
        inheritance = inheritance - (12000 + 50 * age)
    age = age + 1
if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")
