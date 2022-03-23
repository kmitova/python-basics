combination_number = int(input())
counter = 0
flag = False
for a in range(66, 76 + 1):  # B to L
    for b in range(102, 96, -1):  # f to a
        for c in range(65, 67 + 1):  # A to C
            for d in range(1, 10 + 1):  # 1 to 10
                for e in range(10, 1-1, -1):  # 10 to 1
                    if a % 2 == 0:
                        counter += 1
                        if counter == combination_number:
                            prize = a + b + c + d + e
                            print(f"Ticket combination: {chr(a)}{chr(b)}{chr(c)}{d}{e}")
                            print(f"Prize: {prize} lv.")
                            flag = True
                            break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
