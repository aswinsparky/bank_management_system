from model.account import Account

class SavingsAccount(Account):
    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance is None:
            print("Error: Account not found!")
            return
        if amount > current_balance:
            print("Insufficient balance!")
        else:
            new_balance = current_balance - amount
            self.update_balance(new_balance)
            print(f"Withdrawn {amount}. New Balance: {new_balance}")
