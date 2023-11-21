height = float(input("Input height in cm"))
weight = float(input("Input Weight"))

bmi = (weight / ((height / 100) ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi:.2f} you are Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} you are Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} you are Slightly Overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f} you are Obese")
else:
    print(f"Your BMI is {bmi:.2f} you are Clinically Obese")

