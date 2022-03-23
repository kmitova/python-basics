n1 = int(input())
n2 = int(input())
operator = input()
even_odd = 0
result = 0
if n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        print(f"{n1} + {n2} = {result} - even")
    else:
        print(f"{n1} + {n2} = {result} - odd")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} - {n2}  = {result} - even")
    else:
        print(f"{n1} - {n2} = {result} - odd")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} * {n2} = {result} - even")
    else:
        print(f"{n1} * {n2}  = {result} - odd")

elif operator == "/":
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")

