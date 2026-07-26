"""
BMI Calculator (20 points)

Write a program that:
...
"""

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal weight")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")
