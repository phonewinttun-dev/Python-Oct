age = 18
if age >= 18:
    print("You are eligible to vote.")

temperature = 32
if temperature > 30:
    print("It is a hot day. Drink plenty of water.")
else:
    print("The weather is cool and pleasant.")


score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Student Score: {score} -> Grade: {grade}")


# Ticket and ID card verification
# and / or operators
has_ticket = True
has_id_card = False

if has_ticket and has_id_card:
    print("Access allowed: Both ticket and ID verified.")
elif has_ticket or has_id_card:
    print("Access pending: You need both ticket and ID card.")
else:
    print("Access denied: No ticket and no ID card.")

is_account_locked = False
if not is_account_locked:
    print("Account status: Active and ready for use.")


# in / not in operators
fruits = ["apple", "banana", "orange"]

favorite_fruit = "apple"
if favorite_fruit in fruits:
    print(f"{favorite_fruit} is in the fruit list.")

missing_fruit = "mango"
if missing_fruit not in fruits:
    print(f"{missing_fruit} is not in the fruit list.")

# nested if statements
user_logged_in = True
account_balance = 50000
withdraw_amount = 20000

if user_logged_in:
    print("User authenticated successfully.")
    if withdraw_amount > 0:
        if account_balance >= withdraw_amount:
            account_balance -= withdraw_amount
            print(f"Withdrawal completed: {withdraw_amount} MMK")
            print(f"Remaining balance: {account_balance} MMK")
        else:
            print("Error: Insufficient balance.")
    else:
        print("Error: Withdrawal amount must be greater than zero.")
else:
    print("Error: Please log in first.")
