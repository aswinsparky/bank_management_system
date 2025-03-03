from model.db_connection import get_db_connection
from model.transaction import Transaction

class Account:
    def __init__(self, username):
        self.username = username
        self.account_number = self.get_account_number()

    def get_account_number(self):
        """Retrieve the account number from the database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT account_number FROM customers WHERE username = ?", (self.username,))
        account = cursor.fetchone()
        conn.close()
        return account[0] if account else None

    def get_balance(self):
        """Retrieve current balance"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM customers WHERE username = ?", (self.username,))
        balance = cursor.fetchone()
        conn.close()
        return balance[0] if balance else 0

    def deposit(self, amount):
        """Deposit money and save transaction"""
        new_balance = self.get_balance() + amount
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET balance = ? WHERE username = ?", (new_balance, self.username))
        conn.commit()
        conn.close()

        # ✅ Record transaction
        Transaction.record_transaction(self.account_number, "Deposit", amount, new_balance)
        print(f"✅ Deposited {amount}. New Balance: {new_balance}")

    def withdraw(self, amount):
        """Withdraw money and save transaction"""
        current_balance = self.get_balance()
        if amount > current_balance:
            print("❌ Insufficient funds!")
            return

        new_balance = current_balance - amount
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET balance = ? WHERE username = ?", (new_balance, self.username))
        conn.commit()
        conn.close()

        # ✅ Record transaction
        Transaction.record_transaction(self.account_number, "Withdraw", amount, new_balance)
        print(f"✅ Withdrawn {amount}. New Balance: {new_balance}")
