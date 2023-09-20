#!/usr/bin/env python3

while True:
    try:
        age_in_years = int(input("Enter your age in years: "))

        if age_in_years > 0 and age_in_years < 100:
            calc_age = 100 - age_in_years
            print("You will be 100 in", calc_age, "Years")
            again = str(input("Again Y/N?"))
            if again.upper() != "Y":
                break
            else:
                print("Enter your age in years: ")

        else:
            print("Try again")

    except ValueError:
        print("Try again")
    
     
