class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        if amount > 0:
            self.balance += amount
            print("\nAmount Deposited:", amount)
        else:
            print("\nInvalid amount for deposit.")

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance or invalid amount for withdrawal.")

    def display(self):
        print("\nNet Available Balance =", self.balance)

# Driver code
while True:
    s = Bank_Account()
    print("1. Display")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        s.display()
    elif choice == 2:
        s.deposit()
    elif choice == 3:
        s.withdraw()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
