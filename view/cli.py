class CLI:
    def get_customer_info(self):
        print("\nChoose Account Type:\n1. Savings\n2. Current\n3. Loan")
        acc_type = int(input("Enter choice: "))
        name = input("Enter Customer Name: ")
        initial_balance = float(input("Enter initial deposit/loan amount: "))
        return name, acc_type, initial_balance

    def show_menu(self):
        print("\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Exit")
        return int(input("Enter choice: "))

    def get_amount(self, action):
        return float(input(f"Enter amount to {action}: "))
