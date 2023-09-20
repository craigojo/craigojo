#!/usr/bin/env python3
hours = int(input("How many hours did you work?"))
rate = int(input( "How much do you get paid per hour?"))

pay_due = hours * rate

if hours < 10:
    bonus_pay_due = pay_due + rate
    print("Your pay",(f"${bonus_pay_due}"))
elif hours > 100:
    bonus_pay_due = pay_due + (5 * rate)
    print("Your pay",(f"${bonus_pay_due}"))
else:
    print("Your pay",(f"${pay_due}"))





