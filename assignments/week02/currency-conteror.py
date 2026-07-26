"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:
...
"""

direction = input("Choose conversion direction (THB to USD / USD to THB): ")
amount = float(input("Enter amount: "))

exchange_rate = 35.5

if direction == "THB to USD":
    result = amount / exchange_rate
    print(f"{amount:.2f} THB = {result:.2f} USD")
    print(f"Formula: {amount:.2f} / {exchange_rate} = {result:.2f}")

elif direction == "USD to THB":
    result = amount * exchange_rate
    print(f"{amount:.2f} USD = {result:.2f} THB")
    print(f"Formula: {amount:.2f} * {exchange_rate} = {result:.2f}")

else:
    print("Invalid conversion direction")