class BankAccount:
    counter = 1000

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Error: Insufficient balance")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Error: Insufficient balance")


# Input from terminal
name1 = input("Enter first account holder: ")
name2 = input("Enter second account holder: ")

acc1 = BankAccount(name1)
acc2 = BankAccount(name2)

amount1 = float(input("Enter deposit for " + name1 + ": "))
amount2 = float(input("Enter deposit for " + name2 + ": "))

acc1.deposit(amount1)
acc2.deposit(amount2)

withdraw = float(input("Enter withdrawal amount for " + name1 + ": "))
acc1.withdraw(withdraw)

transfer = float(input("Enter transfer amount from " + name1 + " to " + name2 + ": "))
acc1.transfer(transfer, acc2)

print("\n--- Account Details ---")
print("Account Number:", acc1.account_number)
acc1.display_balance()

print("Account Number:", acc2.account_number)
acc2.display_balance()
