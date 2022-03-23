sectors = int(input())
capacity = int(input())
ticket_price = float(input())

total_income = ticket_price * capacity
sector_income = total_income / sectors
charity = (total_income - (sector_income * 0.75)) / 8
print(f"Total income - {total_income:.2f} BGN")
print(f"Money for charity - {charity:.2f} BGN")
