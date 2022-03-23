tshirt = float(input())
sum_for_ball = float(input())

shorts = tshirt * 0.75
socks = shorts * 0.2
shoes = (tshirt + shorts) * 2
total = tshirt + socks + shoes + shorts
total_after_discount = total - total * 0.15
diff = abs(sum_for_ball - total_after_discount)
if total_after_discount >= sum_for_ball:
    print("Yes,he will earn the world-cup replica ball!")
    print(f"His sum is {total_after_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
