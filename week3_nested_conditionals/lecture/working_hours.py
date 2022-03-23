time = int(input())
day = input()

if not day == "Sunday" and 10 <= time <= 18:
    print("open")
else:
    print("closed")
