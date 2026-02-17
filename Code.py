class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
        self.logged_in = False
        self.pin = "1234"
        self.username = "User"

    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.logged_in = True
            print("Authentication successful.")
        else:
            print("Authentication failed.")

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposited: ${amount}')
            print(f'Deposit successful. New balance: ${self.balance}')
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrew: ${amount}')
            print(f'Withdrawal successful. New balance: ${self.balance}')
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def print_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

# Usage example:
# atm = ATM()
# atm.authenticate("1234")
# atm.deposit(500)
# atm.withdraw(200)
# print(f'Balance: ${atm.check_balance()}')
# atm.print_transaction_history()