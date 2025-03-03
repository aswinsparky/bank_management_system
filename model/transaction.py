from model.db_connection import get_db_connection

class Transaction:
    """Handles transaction history for deposits and withdrawals"""

    @staticmethod
    def record_transaction(account_number, trans_type, amount, balance):
        """Record a new transaction in the database"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (account_number, type, amount, balance) VALUES (?, ?, ?, ?)", 
                       (account_number, trans_type, amount, balance))
        conn.commit()
        conn.close()

    @staticmethod
    def get_transaction_history(account_number):
        """Retrieve all past transactions for a user"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT type, amount, balance, timestamp FROM transactions WHERE account_number = ? ORDER BY timestamp DESC", 
                       (account_number,))
        history = cursor.fetchall()
        conn.close()
        return history
