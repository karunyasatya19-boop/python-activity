def run_atm(balance):
    accepted = 0
    rejected = 0
    while True:
        print("\n1. Deposit  2. Withdraw  3. Check balance  4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1" or choice == "2":
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount.")
                rejected += 1
                continue
            if amount <= 0:
                print("Amount must be greater than zero.")
                rejected += 1
            elif choice == "1":
                balance += amount
                accepted += 1
                print(f"Deposit successful. Balance: Rs. {balance:.2f}")
            elif amount <= balance:
                balance -= amount
                accepted += 1
                print(f"Withdrawal successful. Balance: Rs. {balance:.2f}")
            else:
                print("Transaction rejected: insufficient balance.")
                rejected += 1
        elif choice == "3":
            print(f"Available balance: Rs. {balance:.2f}")
        elif choice == "4":
            break
        else:
            print("Choose a valid option from 1 to 4.")
    print("\nATM SUMMARY")
    print(f"Final balance: Rs. {balance:.2f}")
    print("Accepted transactions:", accepted)
    print("Rejected transactions:", rejected)

print("ATM TRANSACTION SIMULATOR")
try:
    opening = float(input("Enter opening balance (Rs.): "))
    if opening < 0:
        print("Opening balance cannot be negative.")
    else:
        run_atm(opening)
except ValueError:
    print("Please enter a valid balance.")
