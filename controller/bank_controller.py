from model.customer import Customer

class BankController:
    def run(self):
        while True:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                customer = Customer(username, password)
                customer.register()  # Assuming you have a register method

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                customer = Customer(username, password)
                
                if customer.login():  # ✅ If login is successful, go to bank menu
                    self.bank_menu(customer)
                else:
                    print("Login failed! Please try again.")

            elif choice == "3":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")


    def bank_menu(self, customer):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                customer.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                customer.withdraw(amount)

            elif choice == "3":
                customer.show_balance()  # Call show_balance method (explained below)

            elif choice == "4":
                print("Logging out...")
                break

            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4.")

