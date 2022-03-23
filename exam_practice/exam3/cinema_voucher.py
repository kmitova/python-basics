voucher_price = int(input())  
movie_tickets = 0
ticket_price = 0
other_items_bought = 0
other_item_price = 0
money_left = 0
command = input()
while command != "End":
    item = command
    item_length = len(item)
    if item_length > 8:
        symbol1 = item[0]
        symbol2 = item[1]
        ticket_price = ord(symbol1) + ord(symbol2)
        if voucher_price < ticket_price:
            break
        else:
            movie_tickets += 1
            voucher_price = voucher_price - ticket_price
    elif item_length <= 8:
        symbol = item[0]
        other_item_price = ord(symbol)
        if voucher_price < other_item_price:
            break
        else:
            other_items_bought += 1
            voucher_price = voucher_price - other_item_price
    command = input()

print(movie_tickets)
print(other_items_bought)
