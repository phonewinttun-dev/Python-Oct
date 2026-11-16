correct_pin = "1234"
account_holder = "Daw Mya"
balance = 100000
transactions = [
    {"type": "Initial Deposit", "amount": 100000, "balance": 100000}
]

attempts = 0
max_attempts = 3
authenticated = False

print("====================================")
print("     WELCOME TO PYTHON BANK ATM     ")
print("====================================")

while attempts < max_attempts:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == correct_pin:
        authenticated = True
        print(f"\nLogin successful. Welcome, {account_holder}!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. You have {remaining} attempt(s) left.\n")
        else:
            print("Incorrect PIN. Your account has been locked for security.")

if not authenticated:
    print("Exiting ATM. Please contact your branch.")
else:
    while True:
        print("\n------------------------------------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        print("------------------------------------")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            print(f"\nAccount Holder: {account_holder}")
            print(f"Current Balance: {balance:,} MMK")

        elif choice == "2":
            deposit_input = input("Enter amount to deposit: ").strip()
            if not deposit_input.isdigit():
                print("Error: Please enter a valid positive number.")
                continue

            deposit_amount = int(deposit_input)
            if deposit_amount <= 0:
                print("Error: Deposit amount must be greater than zero.")
            else:
                balance += deposit_amount
                transactions.append({
                    "type": "Deposit",
                    "amount": deposit_amount,
                    "balance": balance,
                })
                print(f"Successfully deposited {deposit_amount:,} MMK.")
                print(f"Updated Balance: {balance:,} MMK")

        elif choice == "3":
            withdraw_input = input("Enter amount to withdraw: ").strip()
            if not withdraw_input.isdigit():
                print("Error: Please enter a valid positive number.")
                continue

            withdraw_amount = int(withdraw_input)
            if withdraw_amount <= 0:
                print("Error: Withdrawal amount must be greater than zero.")
            elif withdraw_amount > balance:
                print(f"Error: Insufficient funds. Current balance is {balance:,} MMK.")
            else:
                balance -= withdraw_amount
                transactions.append({
                    "type": "Withdrawal",
                    "amount": withdraw_amount,
                    "balance": balance,
                })
                print(f"Successfully withdrew {withdraw_amount:,} MMK.")
                print(f"Remaining Balance: {balance:,} MMK")

        elif choice == "4":
            print("\n============ TRANSACTION HISTORY ============")
            if not transactions:
                print("No transactions recorded yet.")
            else:
                for idx, txn in enumerate(transactions, start=1):
                    txn_type = txn["type"]
                    txn_amount = txn["amount"]
                    txn_bal = txn["balance"]
                    print(f"{idx}. {txn_type:<18} | Amount: {txn_amount:>10,} MMK | Balance: {txn_bal:>10,} MMK")

                total_deposited = 0
                total_withdrawn = 0
                for txn in transactions:
                    if txn["type"] in ["Deposit", "Initial Deposit"]:
                        total_deposited += txn["amount"]
                    elif txn["type"] == "Withdrawal":
                        total_withdrawn += txn["amount"]

                print("--------------------------------------------")
                print(f"Total Deposited: {total_deposited:,} MMK")
                print(f"Total Withdrawn: {total_withdrawn:,} MMK")
                print(f"Net Balance:     {balance:,} MMK")

        elif choice == "5":
            print("\nThank you for using Python Bank ATM. Goodbye!")
            break

        else:
            print("Invalid option selected. Please choose between 1 and 5.")
