open_tabs = int(input())
salary = int(input())

for i in range(open_tabs):
    site = input()
    if site == "Facebook":
        salary = salary - 150
    elif site == "Instagram":
        salary = salary - 100
    elif site == "Reddit":
        salary = salary - 50

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(salary)
