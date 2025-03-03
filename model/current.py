from model.account import Account

class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self.overdraft_limit = 5000

    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance is None:
            print("Error: Account not found!")
            return
        if amount > (current_balance + self.overdraft_limit):
            print("Withdrawal exceeds overdraft limit!")
        else:
            new_balance = current_balance - amount
            self.update_balance(new_balance)
            print(f"Withdrawn {amount}. New Balance: {new_balance}")
