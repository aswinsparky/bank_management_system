from model.account import Account

class LoanAccount(Account):
    def __init__(self, loan_amount):
        super().__init__(balance=-loan_amount)
        self._loan_amount = loan_amount

    def repay_loan(self, amount):
        self._balance += amount
        self.update_balance(self._balance)
        print(f"Loan repayment: {amount}. Remaining Loan Balance: {-self._balance}")

    def withdraw(self, amount):
        print("Cannot withdraw from a loan account!")
