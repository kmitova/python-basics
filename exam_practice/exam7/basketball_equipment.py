yearly_fee = int(input())

sneakers = yearly_fee - yearly_fee * 0.4
clothes = sneakers - sneakers * 0.2
ball = clothes * 0.25
accessories = ball * 0.2

total = yearly_fee + sneakers + clothes + ball + accessories
print(f"{total:.2f}")
