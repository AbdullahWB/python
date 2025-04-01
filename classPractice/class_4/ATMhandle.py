CORRECT_PIN = "1234"
BALANCE = 21000
ACCOUNT_STATUS = "active"
ATM_CASH = 50000
MAX_ATTEMPTS = 3

def authenticate():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == CORRECT_PIN:
            print("PIN verified successfully!")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Please try again. max attempts: {MAX_ATTEMPTS - attempts}")
    print("Too many attempts! your account is locked.")
    return False


def withdraw():
    global BALANCE
    global ATM_CASH
    
    if authenticate():
        if ACCOUNT_STATUS == "active":
            if ATM_CASH > 0:
                day = 0
                while True:
                    try:
                        amount = int(input("Enter withdraw amount: "))
                        if amount == 0:
                            print("You have chosen to cancel the transaction.")
                            break
                        if amount > 0:
                            if amount <= BALANCE:
                                if amount <= ATM_CASH:
                                    if amount > 5000:
                                        print("amount is so big, amount is must be under 5000")
                                    else:
                                        BALANCE -= amount
                                        ATM_CASH -= amount
                                        day+=1
                                        print(f"You have withdrawn {amount}. Your new balance is {BALANCE}. and day is {day}")
                                else:
                                    print("ATM Insufficient balance.")
                                    break
                            else:
                                print("Invalid withdrawal amount.")
                        else:
                            print("Invalid withdraw amount")
                    except ValueError:
                        print("Error! Invalid withdrawal amount.")
            else:
                print("ATM Out of cash.")
        else:
            print("account is frozen.")

withdraw()


# while True:
#     print("1: withdraw money")
#     print("2: check the amount")
    
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         amount("your withdraw amount: ")