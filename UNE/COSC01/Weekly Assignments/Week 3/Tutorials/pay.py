hours_input = input("How many hours did you work? ")
rate_input = input("How much do you get paid per hour? ")

hours = int(hours_input)
rate = float(rate_input)
rate_cents = int(100 * rate) # floats are not exact, so better to use int for currency calculations

pay = hours * rate_cents

if hours < 10:
    pay = pay + 1 * rate_cents
elif hours > 100:
    pay = pay + 5 * rate_cents

pay_dollars = round(pay / 100, 2)
print("Pay due: $", pay_dollars)