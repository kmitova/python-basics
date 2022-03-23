children = 0
adults = 0
command = input()

while command != "Christmas":
    age = int(command)
    if age <= 16:
        children += 1
    else:
        adults += 1
    command = input()

children_money = 5 * children
adults_money = 15 * adults

print(f"Number of adults: {adults}")
print(f"Number of kids: {children}")
print(f"Money for toys: {children_money}")
print(f"Money for sweaters: {adults_money}")
