import json
import os
import datetime

print("\n\nBooting KCC Bank ATM System...")

db_filename = "/Users/mohitkulshreshtha/Desktop/Projects/ATM/atm_database.json"

if os.path.exists(db_filename):
    with open(db_filename, 'r') as file:
        users_db = json.load(file)
else:
    users_db = {
        "1234": {"name": "Mohit", "balance": 5000.0},
        "9876": {"name": "Kartik", "balance": 12000.0},
        "9854": {"name": "xyz", "balance": 12000}
    }
    
    with open(db_filename, 'w') as file:
        json.dump(users_db, file, indent=4) 
            
# ================== FUNCTION =================== #
def save_database(database_dict):
    with open(db_filename, 'w') as file:
        json.dump(database_dict, file, indent=4)

def check_balance(balance):
    print(f"Your Current Balance is : ₹{balance}")

def deposit_cash(pin, amount, current_balance, history_list):
    if amount < 100:
        print("Minimum ₹100 needs to be deposited...")
    else:
        current_balance += amount
        now = datetime.datetime.now()
        time_string = now.strftime("%d-%b-%Y %I:%M %p")
        
        print(f"₹{amount} Deposited. Updated Balance : ₹{current_balance}")
        history_list.append(f"[{time_string}] Deposited: ₹{amount}")
        
    return current_balance, history_list


def withdraw_cash(amount, current_balance, total_withdrawn, daily_limit, history_list):
    if amount > current_balance:
        print("Insufficient fund !!")
    elif (total_withdrawn + amount) > daily_limit:
        print(f"Limit Exceeded !! You can only withdraw ₹{daily_limit - total_withdrawn} more today.")
    else:
        current_balance -= amount
        total_withdrawn += amount
        
        now = datetime.datetime.now()
        time_string = now.strftime("%d-%b-%Y %I:%M %p")
        
        print(f"Please collect ₹{amount}. Remaining Balance: ₹{current_balance}")
        history_list.append(f"[{time_string}] Debited: ₹{amount}")
    return current_balance, total_withdrawn, history_list
    

def transfer_funds(sender_pin, receiver_pin, amount, sender_balance, sender_history, database):
    if receiver_pin not in database:
        print("Error: Receiver account not found!")
        return sender_balance, sender_history, database
        
    if sender_pin == receiver_pin:
        print("Error: You cannot transfer funds to your own account!")
        return sender_balance, sender_history, database
        
    if amount > sender_balance:
        print("Error: Insufficient balance for transfer!")
        return sender_balance, sender_history, database
        
    sender_balance -= amount
    database[receiver_pin]["balance"] += amount
    
    now = datetime.datetime.now()
    time_string = now.strftime("%d-%b-%Y %I:%M %p")
    
    receiver_name = database[receiver_pin]['name']
    sender_history.append(f"[{time_string}] Transferred ₹{amount} to {receiver_name}")
    
    if "history" not in database[receiver_pin]:
        database[receiver_pin]["history"] = []  
        
    sender_name = database[sender_pin]['name']
    database[receiver_pin]["history"].append(f"[{time_string}] Received ₹{amount} from {sender_name}")
    
    print(f"Success! ₹{amount} transferred to {receiver_name}.")
    
    return sender_balance, sender_history, database

# ================================================= #

while True:
    print("\n" + "="*40)
    print("WELCOME TO KCC BANK ATM".center(40))
    print("="*40)
    
    print("1. Login to ATM")
    print("2. Open New Account (Signup)")
    print("0. Shutdown ATM")
    
    start_choice = input("\nSelect an Option: ")
    
    if start_choice == '0':
        print("Shutting down ATM... Good Bye!")
        break
        
    elif start_choice == '2':
        print("\n--- Create New Account ---")
        new_pin = input("Create a 4-digit secret PIN: ")
        
        if new_pin in users_db:
            print("Error: This PIN is already taken! Try another.")
        else:
            new_name = input("Enter your Full Name: ")
            
            users_db[new_pin] = {
                "name": new_name,
                "balance": 0.0,
                "history": []
            }
            
            save_database(users_db)
            print(f"Congratulations {new_name}! Your account is created. You can now Login.")
        continue
            
    elif start_choice == '1':
        daily_limit = 20000.0
        total_withdrawn = 0.0

        if os.path.exists(db_filename):
            with open(db_filename, 'r') as file:
                users_db = json.load(file)
        
        attempt = 0
        is_logged_in = False
        
        while attempt < 3:
            entered_pin = input("Enter your 4-digit PIN: ")

            # FIX: Compare input to string '0', not integer 0
            if entered_pin == '0':
                print("Shutting down ATM... Good Bye!")
                exit() 
                
            if entered_pin in users_db:
                current_user = users_db[entered_pin]["name"]
                account_balance = users_db[entered_pin]["balance"]

                if "history" not in users_db[entered_pin]:
                    users_db[entered_pin]["history"] = []
                transaction_history = users_db[entered_pin]["history"]
                
                print(f"\n>>> Login Successful !! Welcome, {current_user} <<<")
                # FIX: Properly set the login flag to True
                is_logged_in = True 
                break
            else:
                print("Incorrect PIN !!\n")
                attempt += 1

        # FIX: Prevent access to the transaction menu if login failed 3 times
        if not is_logged_in:
            print("Maximum login attempts reached. Returning to main menu.")
            continue
    
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Deposit")
        print("4. Change PIN\n5. Mini Statement\n6. Transfer Fund")
        print("7. Logout / Switch User") 

        choice = int(input("\nSelect an Option : "))

        if choice == 1:
            check_balance(account_balance)


        elif choice == 2:
            amount = float(input("Enter withdrawal amount : "))
            account_balance, total_withdrawn, transaction_history = withdraw_cash(
                amount, account_balance, total_withdrawn, daily_limit, transaction_history)
            users_db[entered_pin]["balance"] = account_balance
            users_db[entered_pin]["history"] = transaction_history
            save_database(users_db)  

                  
        elif choice == 3:
            amount = float(input("Enter Amount : "))
            account_balance, transaction_history = deposit_cash(entered_pin, amount, account_balance, transaction_history)
            users_db[entered_pin]["balance"] = account_balance
            users_db[entered_pin]["history"] = transaction_history
            save_database(users_db)


        elif choice == 4:
            # FIX: Keep PINs as strings to match dictionary keys in JSON database
            previous_pin = input("Enter your Current PIN : ")
            if previous_pin == entered_pin:
                new_pin = input("Enter New PIN : ")
                y = input("Do you really want to proceed (y/n) : ").lower()
                if y == "y":
                    user_data = users_db.pop(entered_pin)
                    users_db[new_pin] = user_data
                    entered_pin = new_pin
                    # FIX: Save the database to persist the new PIN change
                    save_database(users_db)
                    print("\nPIN Updated !!")
                elif y == 'n':
                    print("\nReturning to Main Menu !!")
                else:
                    print("\nInvalid Response !!")
            else:
                print("\nIncorrect PIN !!")


        elif choice == 5:
            print("\n--- Mini Statement (Last 5 Transactions) ---")
            if len(transaction_history) == 0:
                print("No recent transaction!\n")
            else:
                for transaction in transaction_history[-5:]:
                    print(transaction)


        elif choice == 6:
            r_pin = input("Enter Receiver's 4-digit PIN: ")
            transfer_amount = float(input("Enter Amount to Transfer: "))

            account_balance, transaction_history, users_db = transfer_funds(
                entered_pin, r_pin, transfer_amount, account_balance, transaction_history, users_db
            )
            
            users_db[entered_pin]["balance"] = account_balance
            users_db[entered_pin]["history"] = transaction_history
            save_database(users_db)


        elif choice == 7:
            print(f"\nLogging out {current_user}...")
            print("Please take your card. Thank you for using KCC Bank!")
            break
        else:
            print("Invalid Option !!")