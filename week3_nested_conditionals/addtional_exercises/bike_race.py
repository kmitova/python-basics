junior_cyclists = int(input())
senior_cyclists = int(input())
all_cyclists = 0
race_type = input()
junior_fee = 0
senior_fee = 0
total_fee = junior_fee + senior_fee

if race_type == "trail":
    junior_fee = 5.5
    senior_fee = 7
elif race_type == "cross-country":
    junior_fee = 8
    senior_fee = 9.5
elif race_type == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif race_type == "road":
    junior_fee = 20
    senior_fee = 21.5

if race_type == "cross-country" and junior_cyclists + senior_cyclists >= 50:
    overall_income = junior_fee * junior_cyclists + senior_fee * senior_cyclists
    overall_income_with_discount = overall_income - overall_income * 0.25
    taxes = overall_income_with_discount * 0.05
    remaining = overall_income_with_discount - taxes

else:
    overall_income = junior_fee * junior_cyclists + senior_fee * senior_cyclists
    taxes = overall_income * 0.05
    remaining = overall_income - taxes

print(f"{remaining:.2f}")


