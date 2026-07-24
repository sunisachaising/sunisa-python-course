# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if 0<=age<=12 :
    print("Child")
elif 13<=age<=19:
    print("Teenager")
elif 20<=age<60:
    print("Adult")
else :
    print("Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Balance", balance)
        elif choice == "2":
            amount = float(input("Enter amount withdraw: "))
            if amount <=balance:
                balance = balance - amount
                print("Withdrawl successful")
                print("Remaining balance",balance)
            else :
                print("Insufficient balance")

        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            balance = balance + amount
            print("Deposit successful")
            print("New balance:",balance)

        elif choice == "4":
            print("Thank you for using our ATM")
            break
        
else:
    print("Invalid PIN")
