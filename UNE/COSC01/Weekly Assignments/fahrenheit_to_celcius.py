def fahrenheit_to_celcius(temp):
    assert type(temp) in  (int, float)
    assert temp >= -459.67, "Under absolute zero"
    return (temp - 32) / 1.8



print("Hello")





# print(fahrenheit_to_celcius(100))
# print(fahrenheit_to_celcius(-500))


# Assrtions can be turned off ie python3  -0 temp.py
# -0 in the command line turns off assertions