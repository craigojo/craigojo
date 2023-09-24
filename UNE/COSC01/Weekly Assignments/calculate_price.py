def calculate_price(price, order):
    total_price = 0.0
    for item, quantity in order.items():
        if item in price: total_price += price[item] * quantity
        discount = 0.1 if total_price > 100 else (0.05 if 50 < total_price <= 100 else 0)
        total_price -= total_price * discount
    return total_price

price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}

order1 = {'book': 10}
order2 = {'book': 1, 'magazine': 3}
order3 = {'magazine': 5, 'book': 10}

assert(95 == calculate_price(price, order1))
assert(26.5 == calculate_price(price, order2))
assert(114.75 == calculate_price(price, order3))
print("Done")



discount = 0.1 if total_price > 100 else (0.05 if 50 < total_price <= 100 else 0) total_price -= total_price * discount