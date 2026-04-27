

balance = 1000
transactions = []


def check_balance():
    print(f"Current Balance: ₹{balance}")


def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print("Deposit successful")


def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("Withdraw successful")
    else:
        print("Insufficient balance")


def show_statement():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet")
    else:
        for t in transactions:
            print("-", t)


def atm_menu():
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")



atm_menu()