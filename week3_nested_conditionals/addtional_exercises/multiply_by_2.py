from sys import maxsize

for i in range(0, maxsize):
    num = float(input())
    if num >= 0:
        print(f"Result {num * 2:.2f}")
    else:
        print("Negative number!")
