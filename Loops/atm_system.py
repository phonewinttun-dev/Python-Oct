pin = "1234"
balance = 100000
history = ["Initial Balance: 100000 MMK"]

attempts = 3
while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")
    if user_pin == pin:
        print("\nLogin successful!")
        break
    attempts -= 1
    print(f"Wrong PIN. {attempts} attempt(s) left.\n")

if attempts == 0:
    print("Your card is blocked. Please contact support.")
else:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. History")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            print(f"Current Balance: {balance} MMK")

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                history.append(f"Deposit: +{amount} MMK")
                print(f"Deposited {amount} MMK. New Balance: {balance} MMK")
            else:
                print("Amount must be greater than 0.")

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount > balance:
                print("Insufficient funds!")
            elif amount <= 0:
                print("Amount must be greater than 0.")
            else:
                balance -= amount
                history.append(f"Withdraw: -{amount} MMK")
                print(f"Withdrew {amount} MMK. Remaining: {balance} MMK")

        elif choice == "4":
            print("\n--- TRANSACTION HISTORY ---")
            for item in history:
                print(item)

        elif choice == "5":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice, please select 1 to 5.")
