goods_number = int(input())
all_tons = 0
price_train = 0
price_bus = 0
price_truck = 0
bus_goods = 0
truck_goods = 0
train_goods = 0

for goods in range(goods_number):
    tons_per_good = int(input())
    all_tons = all_tons + tons_per_good
    if tons_per_good <= 3:
        bus_goods = bus_goods + tons_per_good
        price_per_ton = 200
        price_bus = price_bus + tons_per_good * 200
    elif tons_per_good <= 11:
        truck_goods = truck_goods + tons_per_good
        price_per_ton = 175
        price_truck = price_truck + tons_per_good * 175
    elif tons_per_good >= 12:
        train_goods = train_goods + tons_per_good
        price_per_ton = 120
        price_train = price_train + tons_per_good * 120

price = price_train + price_truck + price_bus
average_price = price / all_tons
percent_bus = bus_goods / all_tons * 100
percent_truck = truck_goods / all_tons * 100
percent_train = train_goods / all_tons * 100
print(f"{average_price:.2f}")
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
