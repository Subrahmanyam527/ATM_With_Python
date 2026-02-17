import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ATMMachine:
    def __init__(self, balance=0):
        self.balance = balance
        logging.info("ATM initialized with balance: %s", self.balance)
    
    def deposit(self, amount):
        if amount <= 0:
            logging.error("Deposit amount must be positive")
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        logging.info("Deposited %s, new balance is %s", amount, self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            logging.error("Withdrawal amount must be positive")
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            logging.error("Insufficient funds: tried to withdraw %s, but balance is %s", amount, self.balance)
            raise ValueError("Insufficient funds")
        self.balance -= amount
        logging.info("Withdrew %s, new balance is %s", amount, self.balance)

    def check_balance(self):
        logging.info("Checked balance: %s", self.balance)
        return self.balance

# Test cases
if __name__ == "__main__":
    atm = ATMMachine(100)
    try:
        atm.deposit(50)
        atm.withdraw(30)
        print("Current Balance:", atm.check_balance())
        atm.withdraw(150)  # This will raise an error
    except ValueError as e:
        print("Error:", e)