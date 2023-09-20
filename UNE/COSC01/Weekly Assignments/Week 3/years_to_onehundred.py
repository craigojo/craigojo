#!/usr/bin/env python3
age_in_years = int(input("Enter your age in years: "))
if age_in_years > 100:
    print("You've already turned 100!")
elif age_in_years < 0:
    print("Try again after you are born")
else:
    years_to_onehundred = 100 - age_in_years
    print("You will be 100 in",(years_to_onehundred), "years")
